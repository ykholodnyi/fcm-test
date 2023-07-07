## FCM testing project

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1. Add your FCM credentials into root directory as `firebase-adminsdk.json` file
2. Create your `.env` file from `.env.dist`
3. Build docker image:
   ```bash
   docker-compose build
   ```

### Sending messages

1. Run docker container:
   ```bash
   docker-compose run fcm-testing python firebase.py
   ```