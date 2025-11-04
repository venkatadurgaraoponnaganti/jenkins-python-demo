pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "pvdr8978/jenkins-python-demo"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/venkatadurgaraoponnaganti/jenkins-python-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Creating virtual environment..."
                python3 -m venv venv || (echo "python3-venv not found, installing..." && sudo apt update && sudo apt install -y python3.12-venv && python3 -m venv venv)
                . venv/bin/activate

                echo "Fixing pip version for Ubuntu 24.04..."
                rm -rf venv/lib/python3.12/site-packages/pip*
                curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                python get-pip.py pip==23.3.2
                pip install -r requirements.txt
		sh '''
                echo "Fixing permissions for Jenkins (safe mode)..."
		# Only fix script permissions, skip system binaries
		find venv/bin -type f ! -name "python*" -exec chmod +x {} \\;
		'''
		 '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                echo "Running unit tests..."
                chmod +x venv/bin/pytest
                . venv/bin/activate
                venv/bin/pytest -v test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t $DOCKER_IMAGE:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh '''
                    echo "Logging into Docker Hub..."
                    echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin
                    echo "Pushing image to Docker Hub..."
                    docker push $DOCKER_IMAGE:latest
                    docker logout
                    '''
                }
            }
        }

        stage('Build Complete') {
            steps {
                echo '✅ Build, Test, and Docker Push Completed Successfully!'
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed! Check the logs for errors.'
        }
    }
}
