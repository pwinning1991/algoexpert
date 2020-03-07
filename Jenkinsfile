pipeline {
  agent any
  stages {
    stage('Download from git') {
      steps{
          git url: 'https://github.com/pwinning1991/algoexpert'
        }
      }
      stage('Run tests') {
        steps {
         cmake arguments: 'test', installation: 'InSearchPath' 
          }
        }

    }

}
