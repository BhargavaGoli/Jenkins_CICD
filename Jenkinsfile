pipeline {
    agent {
        docker {
            image 'bhargavagoli/dockercli-sonarqube:latest
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        SONAR_URL = 'http://3.85.193.55:9000' 
        DOCKER_IMAGE = "bhargavagoli/jenkinscicd:${BUILD_NUMBER}"
    
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/BhargavaGoli/Jenkins_CICD.git'
            }
        }
        stage('Build') {
            steps {
                sh '''
                    ls -ltr
                    cd app
                    pip install --upgrade pip
                    pip install --no-cache-dir -r requirements.txt
                    '''
            }
        }
        stage('Static code analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube', variable: 'SONAR_TOKEN')]) {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=jenkinscicd \
                    -Dsonar.host.url=${SONAR_URL} \
                    -Dsonar.login=${SONAR_TOKEN}
                    '''
                }
            }
        }
        stage('Docker Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                sh '''
                    docker build -t ${DOCKER_IMAGE} .
                    echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin
                    docker push ${DOCKER_IMAGE}
                '''
                }
            }
        }
        stage('Update Kubernetes Manifests') {
            steps {
                withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]) {
                sh '''
                    git config user.email "bhargava@gmail.com"
                    git config user.name "bhargavagoli"
                    sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" k8s/deployment.yaml
                    git add k8s/deployment.yaml
                    git commit -m "Update deployment to ${DOCKER_IMAGE}"
                    git push https://${GITHUB_TOKEN}@github.com/BhargavaGoli/Jenkins_CICD.git HEAD:main
                '''
                }
            }
        }
    }
    
}
