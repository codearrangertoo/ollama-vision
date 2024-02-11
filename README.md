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
![image sample](http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1461818644od-w480_h360_x2.webp?w=1080&q=75)

The image shows a single-family residential house. It has a two-car garage to the right, which appears to be attached to the main structure of the home. The exterior walls are finished with siding in a light color, possibly cream or tan, while the roof is pitched and made of shingles, suggesting that this could be in a region with colder climates.
The house features several windows visible from the front view. Each window has white trim, which complements the overall color scheme of the house. There are no visible signs or decorations indicating any specific event or time period. The front yard is mostly bare with some fallen leaves scattered on the grass, indicating it might be autumn.
The driveway leading to the garage is clear, and there's a paved sidewalk running parallel to the street in front of the property. There are no visible trees or landscaping features other than the bare branches of a nearby tree. The sky is overcast, suggesting it might be a cloudy day.

