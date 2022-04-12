from kale.common.serveutils import create_inference_service, serve
from kale.common import k8sutils
from kubernetes import client, config

def model_serving(model):
    CO_GROUP = "serving.kubeflow.org"
    CO_VERSION = "v1alpha2"
    CO_PLURAL = "inferenceservices"
    NAMESPACE = 'kubeflow-user'
    MODEL_SERVE_NAME = 'cat-detect'
    
    model.save('/home/jovyan/saved_model_tmp/', overwrite=True)
    
    k8s_co_client = k8sutils.get_co_client()
    try:
        k8s_co_client.delete_namespaced_custom_object(CO_GROUP, CO_VERSION, NAMESPACE, CO_PLURAL, name=MODEL_SERVE_NAME, body=client.V1DeleteOptions())
    except:
        pass
    finally:
        kfserver = serve(model, name=MODEL_SERVE_NAME)
    
    
    return kfserver