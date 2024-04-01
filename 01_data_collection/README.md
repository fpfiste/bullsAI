# Pi-Remote-Camera
Capture photos using your Raspberry Pi camera through a user-friendly Flask web interface. This project allows you to remotely control the camera, capture photos, and provides a gallery for viewing and deleting images. You can easily run the application using Docker Compose.

## Features
* Remote control of the Raspberry Pi camera.
* Capture photos using a user-friendly Flask web interface.
* Photo gallery for viewing and deleting images.
* Easily manage and interact with your photos.

## Prerequisits
Before getting started, make sure you have the following:
* Raspberry Pi with the required peripherals.
* Docker and Docker Compose installed on your Raspberry Pi.
* Raspberry Pi camera module enabled.


## Installing
1. Clone this repository to your Raspberry Pi.
```
git clone https://github.com/yourusername/pi-remote-camera.git
```
2. Navigate to the project directory.
```
cd pi-remote-camera
```
3. Start the application using Docker Compose.
```
docker-compose up -d
```
## Usage
1. Access the web interface by opening a web browser and navigating to http://your-pi-ip-address:7007.
2. Navigate to the camera control section to remotely capture photos.
3. Captured photos are saved and displayed in the photo gallery.
4. In the gallery, you can view and delete images as needed.

## Authors

Fabian Pfister  

## Version History
