pipeline{
    agent{
        docker {
            image 'ubuntu:latest'
            args  '-u root'
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
		apt-get install pip3 -y
		python3 -m pip install -e .
		pip list
		coverage run -m pytest -v --junitxml=report.xml
                '''
            }
       }
    }
}
