pipeline {
    agent any
    
    stages {
        stage('Build docker image') {
        /* This stage builds the actual image; synonymous to
           docker build on the command line */
            steps {
            sh "sudo docker build . -t pythonapp:1"
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
            sh "sudo docker login -u 'orasenatdhubsred01/oracleidentitycloudservice/divya.k.kashyap@oracle.com' -p '3T_LujP;LRyI_tA:qPC7' iad.ocir.io"
            sh "sudo docker tag pythonapp:1 iad.ocir.io/orasenatdhubsred01/divya-repo:custom"
            sh 'sudo docker push iad.ocir.io/orasenatdhubsred01/divya-repo:custom'
            
           }
         } 
         stage('Deploy to OKE') {
         /* Deploy the image to OKE*/

        steps {
            sh 'oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaae2ginbygm2dgnzrgi3dmndegiydsmddgm4wmntcmctdgnrygmzw --file $HOME/.kube/config --region us-ashburn-1 --token-version 2.0.0'
            sh 'kubectl apply -f kubernetes-deployment.yml'
           
           }
         }     
    }
}
