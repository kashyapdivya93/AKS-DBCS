pipeline {
    agent any
    
    stages {
        stage('Build docker image') {
        /* This stage builds the actual image; synonymous to
           docker build on the command line */
            steps {
            sh "docker build . -t pythonapp:${BUILD_NUMBER}"
            }    
        }
        stage('Test image') {
         /* This stage runs unit tests on the image; we are
            just running dummy tests here */
            steps {
                sh 'echo "Tests successful"'
          }
        }
        stage('Push image to OCIR') {
         /* Final stage of build; Push the 
            docker image to our OCI private Registry*/
        steps {
            sh "docker login -u 'orasenatdhubsred01/oracleidentitycloudservice/divya.k.kashyap@oracle.com' -p '3T_LujP;LRyI_tA:qPC7' iad.ocir.io"
            sh "docker tag pythonapp:${BUILD_NUMBER} iad.ocir.io/orasenatdhubsred01/divya-repo:${BUILD_NUMBER}"
            sh 'docker push iad.ocir.io/orasenatdhubsred01/divya-repo:${BUILD_NUMBER}'
            
           }
         } 
         stage('Deploy to OKE') {
         /* Deploy the image to OKE*/

        steps {
		    sh 'export PATH=$PATH:/home/opc/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin && kubectl get nodes && cat kubernetes-deployment.yml | sed "s/{{BUILD_NUMBER}}/${BUILD_NUMBER}/g" | kubectl delete -f - && cat kubernetes-deployment.yml | sed "s/{{BUILD_NUMBER}}/${BUILD_NUMBER}/g" | kubectl apply -f -'
			           
           }
         }     
    }
}
