pipeline{
    agent any{
        docker{
            image 'ubuntu:latest',
            args '-v root'
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