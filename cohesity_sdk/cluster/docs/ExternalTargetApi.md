# cohesity_sdk.ExternalTargetApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_target**](ExternalTargetApi.md#create_external_target) | **POST** /data-protect/external-targets | Create a External Target.
[**delete_external_target**](ExternalTargetApi.md#delete_external_target) | **DELETE** /data-protect/external-targets/{id} | Delete a External Target.
[**get_external_target_by_id**](ExternalTargetApi.md#get_external_target_by_id) | **GET** /data-protect/external-targets/{id} | List details about single External Target.
[**get_external_target_encryption_key_info**](ExternalTargetApi.md#get_external_target_encryption_key_info) | **GET** /data-protect/external-targets/{id}/encryption-key | Get the encryption key info for an external target
[**get_external_target_media_info**](ExternalTargetApi.md#get_external_target_media_info) | **GET** /data-protect/external-targets/media-info | List archive media information
[**get_external_target_settings**](ExternalTargetApi.md#get_external_target_settings) | **GET** /data-protect/external-targets/settings | Get the list of External Target Settings.
[**get_external_targets**](ExternalTargetApi.md#get_external_targets) | **GET** /data-protect/external-targets | Get the list of External Targets.
[**update_external_target**](ExternalTargetApi.md#update_external_target) | **PUT** /data-protect/external-targets/{id} | Update a External Target.
[**update_external_target_settings**](ExternalTargetApi.md#update_external_target_settings) | **PUT** /data-protect/external-targets/settings | Update External Target Settings


# **create_external_target**
> ExternalTarget create_external_target(body)

Create a External Target.

Create a External Target.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.external_target import ExternalTarget
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ExternalTarget() # ExternalTarget | Specifies the parameters to create a External Target.

# example passing only required values which don't have defaults set
try:
	# Create a External Target.
	api_response = client.external_target.create_external_target(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->create_external_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalTarget**](ExternalTarget.md)| Specifies the parameters to create a External Target. |

### Return type

[**ExternalTarget**](ExternalTarget.md)

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

# **delete_external_target**
> delete_external_target(id)

Delete a External Target.

Returns Success if the External Target is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the External Target.
force_delete = True # bool | Specifies whether to force delete the External target. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a External Target.
	client.external_target.delete_external_target(id)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->delete_external_target: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a External Target.
	client.external_target.delete_external_target(id, force_delete=force_delete)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->delete_external_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the External Target. |
 **force_delete** | **bool**| Specifies whether to force delete the External target. | [optional]

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

# **get_external_target_by_id**
> ExternalTarget get_external_target_by_id(id)

List details about single External Target.

Returns the External Target corresponding to the specified Group id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.external_target import ExternalTarget
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the External Target.

# example passing only required values which don't have defaults set
try:
	# List details about single External Target.
	api_response = client.external_target.get_external_target_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->get_external_target_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the External Target. |

### Return type

[**ExternalTarget**](ExternalTarget.md)

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

# **get_external_target_encryption_key_info**
> file_type get_external_target_encryption_key_info(id)

Get the encryption key info for an external target

Get the encryption key info for an external target

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the External Target.

# example passing only required values which don't have defaults set
try:
	# Get the encryption key info for an external target
	api_response = client.external_target.get_external_target_encryption_key_info(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->get_external_target_encryption_key_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the External Target. |

### Return type

**file_type**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_target_media_info**
> ArchivalMediaInfo get_external_target_media_info(cluster_id, cluster_incarnation_id, archival_job_id)

List archive media information

Returns the media information about the specified archive service uid (such as a QStar tape archive service).

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.archival_media_info import ArchivalMediaInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


cluster_id = 1 # int | Specifies the id of the Cohesity cluster which archived to a QStart media target.
cluster_incarnation_id = 1 # int | Specifies the incarnation Id of the Cohesity cluster which archived to a QStart media target.
archival_job_id = 1 # int | Specifies the id of the Job that archived to a QStar media Vault.
restore_task_id = 1 # int | Specifies the id of the restore task to optionally filter by. (optional)
entity_ids = [
        1,
    ] # [int] | Specifies an array of entityIds to optionally filter by. An entityId is a unique id for a VM assigned by the Cohesity Cluster. (optional)

# example passing only required values which don't have defaults set
try:
	# List archive media information
	api_response = client.external_target.get_external_target_media_info(cluster_id, cluster_incarnation_id, archival_job_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->get_external_target_media_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List archive media information
	api_response = client.external_target.get_external_target_media_info(cluster_id, cluster_incarnation_id, archival_job_id, restore_task_id=restore_task_id, entity_ids=entity_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->get_external_target_media_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the id of the Cohesity cluster which archived to a QStart media target. |
 **cluster_incarnation_id** | **int**| Specifies the incarnation Id of the Cohesity cluster which archived to a QStart media target. |
 **archival_job_id** | **int**| Specifies the id of the Job that archived to a QStar media Vault. |
 **restore_task_id** | **int**| Specifies the id of the restore task to optionally filter by. | [optional]
 **entity_ids** | **[int]**| Specifies an array of entityIds to optionally filter by. An entityId is a unique id for a VM assigned by the Cohesity Cluster. | [optional]

### Return type

[**ArchivalMediaInfo**](ArchivalMediaInfo.md)

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

# **get_external_target_settings**
> ExternalTarget get_external_target_settings()

Get the list of External Target Settings.

Get the list of External Target Settings

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.external_target import ExternalTarget
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get the list of External Target Settings.
	api_response = client.external_target.get_external_target_settings()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->get_external_target_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ExternalTarget**](ExternalTarget.md)

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

# **get_external_targets**
> ExternalTargets get_external_targets()

Get the list of External Targets.

Get the list of External Targets.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.external_targets import ExternalTargets
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | Filter by a list of External Target ids. (optional)
global_ids = [
        "globalIds_example",
    ] # [str] | Filter by a list of External Target global ids. (optional)
names = [
        "names_example",
    ] # [str] | Filter by a list of External Target names. (optional)
purpose_types = [
        "Archival",
    ] # [str] | Filter by a list of External Target purpose types. (optional)
storage_types = [
        "Azure",
    ] # [str] | Filter by a list of External Target storage types. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. (optional)
storage_classes = [
        "AmazonS3Standard",
    ] # [str] | Filter by a list of External Target storage classes. (optional)
ownership_contexts = [
        "Local",
    ] # [str] | Specifies whether how this external target is being consumed either Local or FortKnox. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of External Targets.
	api_response = client.external_target.get_external_targets(ids=ids, global_ids=global_ids, names=names, purpose_types=purpose_types, storage_types=storage_types, storage_classes=storage_classes, ownership_contexts=ownership_contexts)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->get_external_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Filter by a list of External Target ids. | [optional]
 **global_ids** | **[str]**| Filter by a list of External Target global ids. | [optional]
 **names** | **[str]**| Filter by a list of External Target names. | [optional]
 **purpose_types** | **[str]**| Filter by a list of External Target purpose types. | [optional]
 **storage_types** | **[str]**| Filter by a list of External Target storage types. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. | [optional]
 **storage_classes** | **[str]**| Filter by a list of External Target storage classes. | [optional]
 **ownership_contexts** | **[str]**| Specifies whether how this external target is being consumed either Local or FortKnox. | [optional]

### Return type

[**ExternalTargets**](ExternalTargets.md)

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

# **update_external_target**
> ExternalTarget update_external_target(id, body)

Update a External Target.

Update the specified External Target.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.external_target import ExternalTarget
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the External Target.
body = ExternalTarget() # ExternalTarget | Specifies the parameters to update a External Target.

# example passing only required values which don't have defaults set
try:
	# Update a External Target.
	api_response = client.external_target.update_external_target(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->update_external_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the External Target. |
 **body** | [**ExternalTarget**](ExternalTarget.md)| Specifies the parameters to update a External Target. |

### Return type

[**ExternalTarget**](ExternalTarget.md)

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

# **update_external_target_settings**
> GlobalBandwidthSettings update_external_target_settings(body)

Update External Target Settings

Update External Target Settings

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.global_bandwidth_settings import GlobalBandwidthSettings
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = GlobalBandwidthSettings(
        archival_params=CommonBandwidthSettings(
            download=BandwidthThrottling(
                rate_limit_bytes_per_sec=1,
                bandwidth_limit_overrides=[
                    BandwidthThrottlingOverride(
                        bytes_per_second=1,
                        time_periods=TimeOfAWeek(
                            days=[
                                "Sunday",
                            ],
                            end_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                            is_all_day=True,
                            start_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                        ),
                    ),
                ],
                timezone="timezone_example",
            ),
            upload=BandwidthThrottling(
                rate_limit_bytes_per_sec=1,
                bandwidth_limit_overrides=[
                    BandwidthThrottlingOverride(
                        bytes_per_second=1,
                        time_periods=TimeOfAWeek(
                            days=[
                                "Sunday",
                            ],
                            end_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                            is_all_day=True,
                            start_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                        ),
                    ),
                ],
                timezone="timezone_example",
            ),
        ),
        tiering_params=CommonBandwidthSettings(
            download=BandwidthThrottling(
                rate_limit_bytes_per_sec=1,
                bandwidth_limit_overrides=[
                    BandwidthThrottlingOverride(
                        bytes_per_second=1,
                        time_periods=TimeOfAWeek(
                            days=[
                                "Sunday",
                            ],
                            end_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                            is_all_day=True,
                            start_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                        ),
                    ),
                ],
                timezone="timezone_example",
            ),
            upload=BandwidthThrottling(
                rate_limit_bytes_per_sec=1,
                bandwidth_limit_overrides=[
                    BandwidthThrottlingOverride(
                        bytes_per_second=1,
                        time_periods=TimeOfAWeek(
                            days=[
                                "Sunday",
                            ],
                            end_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                            is_all_day=True,
                            start_time=TimeOfDay(
                                hour=0,
                                minute=0,
                                time_zone="America/Los_Angeles",
                            ),
                        ),
                    ),
                ],
                timezone="timezone_example",
            ),
        ),
    ) # GlobalBandwidthSettings | Specifies the parameters to update a External Target Settings.

# example passing only required values which don't have defaults set
try:
	# Update External Target Settings
	api_response = client.external_target.update_external_target_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ExternalTargetApi->update_external_target_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalBandwidthSettings**](GlobalBandwidthSettings.md)| Specifies the parameters to update a External Target Settings. |

### Return type

[**GlobalBandwidthSettings**](GlobalBandwidthSettings.md)

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

