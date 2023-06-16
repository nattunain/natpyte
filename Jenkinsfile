pipeline{
    agent {
        docker {
            image 'ubuntu:latest'
        }
    }
    stages{
        stage('First Stage'){
            steps{
                sh'Develop stage'
            }
        }

        stage('Test Stage'){
            steps{
                sh 'Test Stage'
            }
        }

        stage('Deploy Stage'){
            steps{
                sh 'Deploy Stage'
            }
        }
    }
}