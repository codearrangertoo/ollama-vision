# ollama-vision
Ollama-Vision is an innovative Python project that marries the capabilities of Docker and Python to offer a seamless, efficient process for image and video analysis through the Ollama service and Llava model. This project not only streamlines the fetching, processing, and analyzing of images or the first frames of videos from web URLs and local storage but also utilizes an advanced Large Language Model (LLM) for descriptive analysis of the visual content. With its robust Docker and microservice architecture, Ollama-Vision encapsulates services for image downloading, conversion, and detailed analysis within a Dockerized environment, significantly simplifying the setup process for users.

The tool is designed with a keen focus on dynamic media handling, capable of distinguishing between images and videos, and adeptly uses PIL (Python Imaging Library) and OpenCV for image and video frame conversion, ensuring the media is ready for analysis. Images are converted to Base64 strings to facilitate their transmission to the LLM, showcasing an application of AI in understanding and narrating visual content. This integration with the Langchain Community's Ollama LLM exemplifies the potential of AI in generating textual descriptions of images, enhancing digital media management and content creation.

Moreover, Ollama-Vision is optimized for performance, offering integration with NVIDIA GPU for accelerated computing, making it an ideal choice for developers and researchers in need of an out-of-the-box solution for advanced image analysis tasks. The project's modular design allows for easy modification and expansion, demonstrating excellent software engineering practices suitable for a wide range of applications, from AI-driven analysis platforms to content generation.

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
##### Input Image
![image sample](http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1461818644od-w480_h360_x2.webp?w=1080&q=75)
##### LLaVA LLM description:
The image shows a single-family residential house. It has a two-car garage to the right, which appears to be attached to the main structure of the home. The exterior walls are finished with siding in a light color, possibly cream or tan, while the roof is pitched and made of shingles, suggesting that this could be in a region with colder climates.
The house features several windows visible from the front view. Each window has white trim, which complements the overall color scheme of the house. There are no visible signs or decorations indicating any specific event or time period. The front yard is mostly bare with some fallen leaves scattered on the grass, indicating it might be autumn.
The driveway leading to the garage is clear, and there's a paved sidewalk running parallel to the street in front of the property. There are no visible trees or landscaping features other than the bare branches of a nearby tree. The sky is overcast, suggesting it might be a cloudy day.

