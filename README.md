# blink-camera-explore
Exploring using the api for the blink camera product from amazon.

# Use


## Build
```
docker build -t blinktemp .
```

## Setup env file

Edit "env.list"

```
BLINK_USERNAME=fake
BLINK_PASSWORD=fake
BLINK_CAMERA_NAME=camera name
```

## Run
```
docker run --env-file ./env.list -v ${PWD}/data:/data blinktemp
```
