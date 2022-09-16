# cohesity_sdk.SourceApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_protection_source_registration**](SourceApi.md#patch_protection_source_registration) | **PATCH** /data-protect/sources/registrations/{id} | Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra


# **patch_protection_source_registration**
> CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08 patch_protection_source_registration(id, body)

Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra

Patches a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.source_registration_patch_request_params import SourceRegistrationPatchRequestParams
from cohesity_sdk.cluster.model.common_source_registration_reponse_paramsbb51eef19bdd4e3f_b5257fcc70fe0a08 import CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protection Source registration.
body = SourceRegistrationPatchRequestParams(
        environment="kVMware",
        cassandra_params=CassandraSourceRegistrationPatchParams(
            seed_node="seed_node_example",
            config_directory="config_directory_example",
            dse_configuration_directory="dse_configuration_directory_example",
            is_dse_tiered_storage=True,
            is_dse_authenticator=True,
            ssh_password_credentials=SshPasswordCredentials(
                username="username_example",
                password="password_example",
            ),
            ssh_private_key_credentials=SshPrivateKeyCredentials(
                user_id="user_id_example",
                private_key="private_key_example",
                passphrase="passphrase_example",
            ),
            jmx_credentials=CassandraSourceRegistrationPatchParamsJmxCredentials(
                password="password_example",
                username="username_example",
            ),
            cassandra_credentials=CassandraSourceRegistrationPatchParamsCassandraCredentials(
                password="password_example",
                username="username_example",
            ),
            data_center_names=[
                "data_center_names_example",
            ],
            commit_log_backup_location="commit_log_backup_location_example",
            kerberos_principal="kerberos_principal_example",
            dse_solr_info=DSESolrInfo(
                solr_nodes=[
                    "solr_nodes_example",
                ],
                solr_port=1,
            ),
        ),
    ) # SourceRegistrationPatchRequestParams | Specifies the parameters to partially update the registration.

# example passing only required values which don't have defaults set
try:
	# Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
	api_response = client.source.patch_protection_source_registration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SourceApi->patch_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. |
 **body** | [**SourceRegistrationPatchRequestParams**](SourceRegistrationPatchRequestParams.md)| Specifies the parameters to partially update the registration. |

### Return type

[**CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08**](CommonSourceRegistrationReponseParamsbb51eef19bdd4e3fB5257fcc70fe0a08.md)

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

