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
		python3 -m pip3 install -e .
		pip3 list
		coverage run -m pytest -v --junitxml=report.xml
                '''
            }
       }
    }
}
