# cohesity_sdk.SecurityApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_clientcsr**](SecurityApi.md#create_clientcsr) | **POST** /clientcsr | Create Certificate Signing Requests on the cluster.
[**create_csr**](SecurityApi.md#create_csr) | **POST** /csr | Create a Certificate Signing Request on the cluster.
[**delete_csr**](SecurityApi.md#delete_csr) | **DELETE** /csr/{id} | Delete a Certificate Signing Request on the cluster.
[**get_ciphers**](SecurityApi.md#get_ciphers) | **GET** /security/ciphers | Gets the list of ciphers enabled on the cluster.
[**get_csr_by_id**](SecurityApi.md#get_csr_by_id) | **GET** /csr/{id} | List the specified Certificate Signing Request.
[**get_csr_list**](SecurityApi.md#get_csr_list) | **GET** /csr | List Certificate Signing Requests on the cluster.
[**get_object_store_ciphers**](SecurityApi.md#get_object_store_ciphers) | **GET** /security/object-store-ciphers | Gets the list of object store ciphers enabled on the cluster.
[**get_security_config**](SecurityApi.md#get_security_config) | **GET** /security-config | Get cluster security settings.
[**import_certificate_by_clientcsr**](SecurityApi.md#import_certificate_by_clientcsr) | **POST** /clientcsr/certificate | Import the signed certificates on the cluster after the Certificate Signing Requests are created.
[**list_trusted_ca_by_id**](SecurityApi.md#list_trusted_ca_by_id) | **GET** /trusted-cas/{id} | List the specified Certificate.
[**list_trusted_cas**](SecurityApi.md#list_trusted_cas) | **GET** /trusted-cas | List all Certificates with cluster trust store.
[**modify_ciphers**](SecurityApi.md#modify_ciphers) | **POST** /security/ciphers | Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
[**modify_object_store_ciphers**](SecurityApi.md#modify_object_store_ciphers) | **POST** /security/object-store-ciphers | Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.
[**register_trusted_cas**](SecurityApi.md#register_trusted_cas) | **POST** /trusted-cas | Register CA Certificate to the cluster trust store.
[**unregister_trusted_ca**](SecurityApi.md#unregister_trusted_ca) | **DELETE** /trusted-cas/{id} | Unregister CA Certificate from the cluster trust store.
[**update_certificate_by_csr**](SecurityApi.md#update_certificate_by_csr) | **POST** /csr/certificate | Update the signed certificate on the cluster after a Certificate Signing Request is created.
[**update_security_config**](SecurityApi.md#update_security_config) | **PUT** /security-config | Update cluster security settings.
[**validate_trusted_ca_by_id**](SecurityApi.md#validate_trusted_ca_by_id) | **POST** /trusted-cas/{id}/validate | Validate CA Certificate.


# **create_clientcsr**
> CreateClientcsrResponseBody create_clientcsr(body)

Create Certificate Signing Requests on the cluster.

Create two Certificate Signing Request on the cluster with the given details one each for client and server. Each service can have at most one outstanding pair of CSR.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_clientcsr_response_body import CreateClientcsrResponseBody
from cohesity_sdk.helios.model.create_csr_request import CreateCsrRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateCsrRequest() # CreateCsrRequest | Specifies the parameters to create the Certificate Signing Requests.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create Certificate Signing Requests on the cluster.
	api_response = client.security.create_clientcsr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->create_clientcsr: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create Certificate Signing Requests on the cluster.
	api_response = client.security.create_clientcsr(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->create_clientcsr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCsrRequest**](CreateCsrRequest.md)| Specifies the parameters to create the Certificate Signing Requests. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CreateClientcsrResponseBody**](CreateClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_csr**
> CreateCsrResponseBody create_csr(body)

Create a Certificate Signing Request on the cluster.

Create a Certificate Signing Request on the cluster with the given details. Each service has at most one outstanding CSR.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_csr_response_body import CreateCsrResponseBody
from cohesity_sdk.helios.model.create_csr_request import CreateCsrRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateCsrRequest() # CreateCsrRequest | Specifies the parameters to create a Certificate Signing Request.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Certificate Signing Request on the cluster.
	api_response = client.security.create_csr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->create_csr: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Certificate Signing Request on the cluster.
	api_response = client.security.create_csr(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->create_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCsrRequest**](CreateCsrRequest.md)| Specifies the parameters to create a Certificate Signing Request. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CreateCsrResponseBody**](CreateCsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_csr**
> delete_csr(id)

Delete a Certificate Signing Request on the cluster.

Delete a Certificate Signing Request on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the csr to be deleted.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a Certificate Signing Request on the cluster.
	client.security.delete_csr(id)
except ApiException as e:
	print("Exception when calling SecurityApi->delete_csr: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Certificate Signing Request on the cluster.
	client.security.delete_csr(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling SecurityApi->delete_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr to be deleted. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ciphers**
> CiphersResp get_ciphers()

Gets the list of ciphers enabled on the cluster.

Gets the list of ciphers enabled on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.ciphers_resp import CiphersResp
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Gets the list of ciphers enabled on the cluster.
	api_response = client.security.get_ciphers(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CiphersResp**](CiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_by_id**
> CommonCsrResponseParams get_csr_by_id(id)

List the specified Certificate Signing Request.

List the specified Certificate Signing Request.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.common_csr_response_params import CommonCsrResponseParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the csr.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List the specified Certificate Signing Request.
	api_response = client.security.get_csr_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_csr_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the specified Certificate Signing Request.
	api_response = client.security.get_csr_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_csr_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CommonCsrResponseParams**](CommonCsrResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_list**
> GetCsrListResponseBody get_csr_list()

List Certificate Signing Requests on the cluster.

List Certificate Signing Requests on the cluster with service name filtering.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_csr_list_response_body import GetCsrListResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
service_name = "iris" # str | Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. (optional) if omitted the server will use the default value of "iris"
ids = [
        "ids_example",
    ] # [str] | Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Certificate Signing Requests on the cluster.
	api_response = client.security.get_csr_list(access_cluster_id=access_cluster_id, region_id=region_id, service_name=service_name, ids=ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_csr_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **service_name** | **str**| Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. | [optional] if omitted the server will use the default value of "iris"
 **ids** | **[str]**| Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. | [optional]

### Return type

[**GetCsrListResponseBody**](GetCsrListResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_store_ciphers**
> ObjectStoreCiphersResp get_object_store_ciphers()

Gets the list of object store ciphers enabled on the cluster.

Gets the list of object store ciphers enabled on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.object_store_ciphers_resp import ObjectStoreCiphersResp
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Gets the list of object store ciphers enabled on the cluster.
	api_response = client.security.get_object_store_ciphers(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_object_store_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ObjectStoreCiphersResp**](ObjectStoreCiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_config**
> SecurityConfigResponse get_security_config()

Get cluster security settings.

Get cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.security_config_response import SecurityConfigResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get cluster security settings.
	api_response = client.security.get_security_config(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_security_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SecurityConfigResponse**](SecurityConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_certificate_by_clientcsr**
> ImportCertificateByClientcsrResponseBody import_certificate_by_clientcsr(body)

Import the signed certificates on the cluster after the Certificate Signing Requests are created.

Import the signed certificates on the cluster after the Certificate Signing Requests are created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.import_certificate_by_clientcsr_response_body import ImportCertificateByClientcsrResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.import_certificate_by_clientcsr_request import ImportCertificateByClientcsrRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ImportCertificateByClientcsrRequest(
        certificate_server="certificate_server_example",
        certificate_client="certificate_client_example",
    ) # ImportCertificateByClientcsrRequest | Specifies the parameters to import the certificate.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Import the signed certificates on the cluster after the Certificate Signing Requests are created.
	api_response = client.security.import_certificate_by_clientcsr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->import_certificate_by_clientcsr: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Import the signed certificates on the cluster after the Certificate Signing Requests are created.
	api_response = client.security.import_certificate_by_clientcsr(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->import_certificate_by_clientcsr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportCertificateByClientcsrRequest**](ImportCertificateByClientcsrRequest.md)| Specifies the parameters to import the certificate. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ImportCertificateByClientcsrResponseBody**](ImportCertificateByClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trusted_ca_by_id**
> TrustedCa list_trusted_ca_by_id(id)

List the specified Certificate.

List the specified Certificate.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.trusted_ca import TrustedCa
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the certificate.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List the specified Certificate.
	api_response = client.security.list_trusted_ca_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->list_trusted_ca_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List the specified Certificate.
	api_response = client.security.list_trusted_ca_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->list_trusted_ca_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**TrustedCa**](TrustedCa.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trusted_cas**
> ListTrustedCasResult list_trusted_cas()

List all Certificates with cluster trust store.

List all trusted certificates in cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.list_trusted_cas_result import ListTrustedCasResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        "ids_example",
    ] # [str] | Specifies the ids of the certificates to be returned. (optional)
names = [
        "names_example",
    ] # [str] | Specifies the names of the certificates to be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List all Certificates with cluster trust store.
	api_response = client.security.list_trusted_cas(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, names=names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->list_trusted_cas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[str]**| Specifies the ids of the certificates to be returned. | [optional]
 **names** | **[str]**| Specifies the names of the certificates to be returned. | [optional]

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_ciphers**
> CiphersResp modify_ciphers(body)

Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.

Enable/Disable a list of ciphers on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.modify_ciphers_request_body import ModifyCiphersRequestBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.ciphers_resp import CiphersResp
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ModifyCiphersRequestBody(
        enable=True,
        ciphers=[
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        ],
    ) # ModifyCiphersRequestBody | Enable/Disable ciphers.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
	api_response = client.security.modify_ciphers(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->modify_ciphers: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
	api_response = client.security.modify_ciphers(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->modify_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyCiphersRequestBody**](ModifyCiphersRequestBody.md)| Enable/Disable ciphers. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**CiphersResp**](CiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_object_store_ciphers**
> ObjectStoreCiphersResp modify_object_store_ciphers(body)

Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.

Enable/Disable a list of object store ciphers on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.object_store_ciphers_resp import ObjectStoreCiphersResp
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.modify_object_store_ciphers_request_body import ModifyObjectStoreCiphersRequestBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ModifyObjectStoreCiphersRequestBody(
        enable=True,
        ciphers=[
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        ],
    ) # ModifyObjectStoreCiphersRequestBody | Enable/Disable object store ciphers.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.
	api_response = client.security.modify_object_store_ciphers(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->modify_object_store_ciphers: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.
	api_response = client.security.modify_object_store_ciphers(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->modify_object_store_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyObjectStoreCiphersRequestBody**](ModifyObjectStoreCiphersRequestBody.md)| Enable/Disable object store ciphers. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ObjectStoreCiphersResp**](ObjectStoreCiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_trusted_cas**
> ListTrustedCasResult register_trusted_cas(body)

Register CA Certificate to the cluster trust store.

Register CA Certificate to the cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.list_trusted_cas_result import ListTrustedCasResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.register_trusted_cas import RegisterTrustedCas
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = RegisterTrustedCas(
        certificates=[
            TrustedCaRequest(
                certificate="certificate_example",
                name="name_example",
                description="description_example",
            ),
        ],
        only_validate=True,
    ) # RegisterTrustedCas | Specifies the parameters to register a Certificate.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Register CA Certificate to the cluster trust store.
	api_response = client.security.register_trusted_cas(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->register_trusted_cas: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Register CA Certificate to the cluster trust store.
	api_response = client.security.register_trusted_cas(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->register_trusted_cas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterTrustedCas**](RegisterTrustedCas.md)| Specifies the parameters to register a Certificate. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_trusted_ca**
> unregister_trusted_ca(id)

Unregister CA Certificate from the cluster trust store.

Unregister CA Certificate from the cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the certificate to be unregistered.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Unregister CA Certificate from the cluster trust store.
	client.security.unregister_trusted_ca(id)
except ApiException as e:
	print("Exception when calling SecurityApi->unregister_trusted_ca: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Unregister CA Certificate from the cluster trust store.
	client.security.unregister_trusted_ca(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling SecurityApi->unregister_trusted_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be unregistered. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_by_csr**
> UpdateCertificateByCsrResponseBody update_certificate_by_csr(body)

Update the signed certificate on the cluster after a Certificate Signing Request is created.

Update the signed certificate on the cluster after a Certificate Signing Request is created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_certificate_by_csr_request import UpdateCertificateByCsrRequest
from cohesity_sdk.helios.model.update_certificate_by_csr_response_body import UpdateCertificateByCsrResponseBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UpdateCertificateByCsrRequest(
        certificate="certificate_example",
        csr_id="csr_id_example",
    ) # UpdateCertificateByCsrRequest | Specifies the parameters to update the certificate.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update the signed certificate on the cluster after a Certificate Signing Request is created.
	api_response = client.security.update_certificate_by_csr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->update_certificate_by_csr: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update the signed certificate on the cluster after a Certificate Signing Request is created.
	api_response = client.security.update_certificate_by_csr(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->update_certificate_by_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCertificateByCsrRequest**](UpdateCertificateByCsrRequest.md)| Specifies the parameters to update the certificate. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UpdateCertificateByCsrResponseBody**](UpdateCertificateByCsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_security_config**
> SecurityConfigResponse update_security_config(body)

Update cluster security settings.

Update cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.update_security_config_request import UpdateSecurityConfigRequest
from cohesity_sdk.helios.model.security_config_response import SecurityConfigResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UpdateSecurityConfigRequest() # UpdateSecurityConfigRequest | Specifies the parameters to update security config.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update cluster security settings.
	api_response = client.security.update_security_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->update_security_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update cluster security settings.
	api_response = client.security.update_security_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->update_security_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSecurityConfigRequest**](UpdateSecurityConfigRequest.md)| Specifies the parameters to update security config. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**SecurityConfigResponse**](SecurityConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_trusted_ca_by_id**
> TrustedCa validate_trusted_ca_by_id(id)

Validate CA Certificate.

Certificate will be checked for Expiration and Revocation.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.trusted_ca import TrustedCa
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the certificate to be validated.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Validate CA Certificate.
	api_response = client.security.validate_trusted_ca_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->validate_trusted_ca_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Validate CA Certificate.
	api_response = client.security.validate_trusted_ca_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->validate_trusted_ca_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be validated. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**TrustedCa**](TrustedCa.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

