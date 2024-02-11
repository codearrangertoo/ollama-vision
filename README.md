# ollama-vision
Ollama-Vision is a robust Docker and Python-based project designed to streamline the process of image analysis using the cutting-edge Ollama service and Llava model. It showcases a microservice architecture, encapsulating services for image downloading, conversion, and analysis within a Dockerized environment. This project simplifies the setup process, offering a seamless integration with NVIDIA GPU for accelerated computing. It's perfect for developers and researchers looking for an out-of-the-box solution for advanced image analysis tasks. With Ollama-Vision, embark on a journey of efficient image processing, leveraging the power of modern machine learning models and Docker's versatility.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Supported NVIDIA GPU
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Build and start services
```
docker compose up
```

* You will need to wait some time while ollama downloads the llava model

#### Example output
![image sample](http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3560213744od-w480_h360_x2.webp?w=1080&q=75)

The image shows a heating and cooling system installed in what appears to be an attic or basement space. There are two main components visible:
1. An air conditioning unit (likely a split-style unit) positioned on the left side of the frame, with its condensing coils and compressor unit visible, as well as the electrical connections for power.
2. A gas boiler installed in the center and to the right, with pipes leading away from it. The boiler has a yellow sticker indicating some type of warning or instruction, but the text is not legible in this image. It also displays the "Bradford White" branding on its side.
3. The system appears to be well-organized and possibly professionally installed, as indicated by the clear piping and safety measures such as the yellow sticker. The environment looks unfinished, suggesting that this could be a workspace or an area where maintenance takes place.

