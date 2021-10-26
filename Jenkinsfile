pipeline {
	agent any
    triggers{
        pollSCM('* * * * *')
        cron('0 0 * * *')                   //    https://crontab.guru/#0_0_*_*_*
    }
 	stages {
 		stage("Compile") {
 			steps {
 				echo "python code"
 			}
 		}
 		stage("Unit test") {
 			steps {
 				sh "python test.py"
 			}
 		}
 	}
}
