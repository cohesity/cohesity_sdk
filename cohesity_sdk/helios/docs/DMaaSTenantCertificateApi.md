# cohesity_sdk.DMaaSTenantCertificateApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dmaas_tenant_cert**](DMaaSTenantCertificateApi.md#add_dmaas_tenant_cert) | **POST** /dmaas-tenant-certificate | Add a DMaaS tenant certificate to the cluster.
[**delete_dmaas_tenant_cert**](DMaaSTenantCertificateApi.md#delete_dmaas_tenant_cert) | **DELETE** /dmaas-tenant-certificate/{tenantId} | Delete a tenant certificate.
[**get_dmaas_tenant_certs**](DMaaSTenantCertificateApi.md#get_dmaas_tenant_certs) | **GET** /dmaas-tenant-certificate | Get DMaaS tenant certificates on the cluster.


# **add_dmaas_tenant_cert**
> AddDmaasTenantCertRequest add_dmaas_tenant_cert(body)

Add a DMaaS tenant certificate to the cluster.

Add a DMaaS tenant certificate to the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.add_dmaas_tenant_cert_request import AddDmaasTenantCertRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = AddDmaasTenantCertRequest(
        tenant_id="tenant_id_example",
        certificate="certificate_example",
        private_key="private_key_example",
        connector_ca_chain="connector_ca_chain_example",
        passphrase="passphrase_example",
    ) # AddDmaasTenantCertRequest | Specifies the parameters to add the tenant certificate.

# example passing only required values which don't have defaults set
try:
	# Add a DMaaS tenant certificate to the cluster.
	api_response = client.d_maa_s_tenant_certificate.add_dmaas_tenant_cert(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DMaaSTenantCertificateApi->add_dmaas_tenant_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDmaasTenantCertRequest**](AddDmaasTenantCertRequest.md)| Specifies the parameters to add the tenant certificate. |

### Return type

[**AddDmaasTenantCertRequest**](AddDmaasTenantCertRequest.md)

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

# **delete_dmaas_tenant_cert**
> delete_dmaas_tenant_cert(tenant_id)

Delete a tenant certificate.

Delete a tenant certificate.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


tenant_id = "tenantId_example" # str, none_type | Specifies the id of tenant.

# example passing only required values which don't have defaults set
try:
	# Delete a tenant certificate.
	client.d_maa_s_tenant_certificate.delete_dmaas_tenant_cert(tenant_id)
except ApiException as e:
	print("Exception when calling DMaaSTenantCertificateApi->delete_dmaas_tenant_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str, none_type**| Specifies the id of tenant. |

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

# **get_dmaas_tenant_certs**
> TenantDmaasCerts get_dmaas_tenant_certs()

Get DMaaS tenant certificates on the cluster.

Get DMaaS tenant certificates on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_dmaas_certs import TenantDmaasCerts
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which tenants are returned. If no tenant id is specified, all tenant certificates are returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get DMaaS tenant certificates on the cluster.
	api_response = client.d_maa_s_tenant_certificate.get_dmaas_tenant_certs(tenant_ids=tenant_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DMaaSTenantCertificateApi->get_dmaas_tenant_certs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which tenants are returned. If no tenant id is specified, all tenant certificates are returned. | [optional]

### Return type

[**TenantDmaasCerts**](TenantDmaasCerts.md)

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

