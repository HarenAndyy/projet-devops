pipeline {
    agent any

    environment {
        IMAGE_NAME = "app-devops"
        CONTAINER_NAME = "app-devops-container"
        PORT = "8082"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/HarenAndyy/projet-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} -f docker/Dockerfile .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run -d --name test-container -p 9091:80 ${IMAGE_NAME}
                    sleep 3
                    curl -f http://localhost:9091 || exit 1
                    docker stop test-container
                    docker rm test-container
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p ${PORT}:80 ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        failure {
            echo 'Pipeline échoué — vérifier les logs'
        }
        success {
            echo 'Déploiement réussi !'
        }
    }
}
