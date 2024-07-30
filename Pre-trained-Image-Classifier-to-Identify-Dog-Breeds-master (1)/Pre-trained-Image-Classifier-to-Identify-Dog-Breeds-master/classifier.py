import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load pretrained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

model_dict = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as file:
    imagenet_classes = ast.literal_eval(file.read())


def classifier(img_path, model_name):
    # Open the image file
    image = Image.open(img_path)

    # Define the preprocessing transformations
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Apply the transformations to the image
    image_tensor = preprocess(image)

    # Add a batch dimension to the tensor
    image_tensor = image_tensor.unsqueeze(0)

    # Check PyTorch version
    pytorch_version = __version__.split('.')

    # For PyTorch version 0.4 and above
    if int(pytorch_version[0]) > 0 or int(pytorch_version[1]) >= 4:
        image_tensor.requires_grad_(False)
    else:
        # For PyTorch versions below 0.4
        image_tensor = Variable(image_tensor, volatile=True)

    # Select the model
    model = model_dict[model_name]

    # Set the model to evaluation mode
    model.eval()

    # Perform inference
    if int(pytorch_version[0]) > 0 or int(pytorch_version[1]) >= 4:
        output = model(image_tensor)
    else:
        output = model(image_tensor)

    # Get the predicted class index
    _, predicted_idx = output.max(1)
    predicted_idx = predicted_idx.item()

    # Return the human-readable label of the predicted class
    return imagenet_classes[predicted_idx]
