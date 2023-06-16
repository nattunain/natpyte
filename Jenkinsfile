pipeline{
    agent {
        docker {
            image 'ubuntu:latest'
        }
    }

    environment {
        now = sh(returnStdout: true, script: "date '+%Y%m%d'")
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
                  pip list
                  python3 -m pip install -e .
                  coverage run -m pytest --capture=no --junitxml=report.xml
                '''
            }
        }
        
    }
}