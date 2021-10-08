# docker-registry-prv
A repo containing information and tools that help with building self hosted private Docker registry

**This doc is under construction**

Server side steps:
1. Prepare CA cert for Your private https registry
```
openssl req   -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key   -addext "subjectAltName = DNS:customreg.epi.local"   -x509 -days 365 -out certs/domain.crt
```
2. Copy the the containers into the loccal folder and then rUn the python sccript tha twill load docker tar files into Your registry

sudo docker run -d -e REGISTRY_HTTP_ADDR=0.0.0.0:5010 -e REGISTRY_HTTP_TLS_CERTIFICATE=/custom-repo/certs/domain.crt -e REGISTRY_HTTP_TLS_KEY=/custom-repo/certs/domain.key \-p 5010:5010 --restart=always  --name ubu1804-custreg -v /custom-repo/certs:/custom-repo/certs -v /custom-repo/ubuntu-18.04/images:/var/lib/registry registry:2


Na kliencie:
cat > /etc/docker/certs.d/myregistry.domain.com:5010/ca.crt
docker pull customreg.epi.local:5010/vault-1.6.1
