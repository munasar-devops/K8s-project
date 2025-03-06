
# create a script that check if a pod is down or running 
import time 
from kubernetes import client, config

# Load the k8s config 

config.load_kube_config()

# create api 
v1 = client.CoreV1Api()

# set namespace

namespace = "test-demo"
pod_name = "frontend"

try:
    pod_name = v1.read_namespaced_pod_status(name=pod_name, namespace=namespace)
    pod_status = pod_name.status.phase 


    if pod_name == "Running":
        print(f'{pod_name} is running!')
    else:
        print(f" ✅ pod {pod_name} is in status {pod_status}")

except client.exceptions.ApiException as e:
    print(f"Error: {e.reason} - pod {pod_name} might not be exist in the API error occured.")

print()