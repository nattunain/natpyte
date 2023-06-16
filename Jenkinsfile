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

        stage('Build Stage'){
            when {
                branch 'dev'
            }
            steps{
                sh ''' 
                  apt-get update
                  apt-get -y install python3
                  pip3 install -e .
                  coverage run -m pytest --capture=no --junitxml=report.xml
                '''
            }
        }
        
    }
}