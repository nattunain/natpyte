pipeline{
    agent{
        docker {
            image 'ubuntu:latest'
        }
    }
    stages {
        stage('test'){
            when {
                branch 'dev'
            }      
            steps{
                sh '''
                apt-get update
                apt-get install python3 -y
                '''
            }
       }
    }
}