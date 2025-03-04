# HbaseSourceRegistrationParams

Specifies parameters to register an HBase source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authentication type. | [optional] [readonly] 
**data_root_directory** | **str** | The &#39;Data root directory&#39; for this HBase. | [optional] [readonly] 
**zookeeper_quorum** | **List[str]** | The &#39;Zookeeper Quorum&#39; for this HBase. | [optional] [readonly] 
**configuration_directory** | **str** | The directory containing the hbase-site.xml. | 
**hdfs_source_registration_id** | **int** | Protection Source registration id of the HDFS on which this HBase is running. | 
**host** | **str** | IP or hostname of any host from which the HBase configuration file hbase-site.xml can be read. | 
**kerberos_principal** | **str** | The kerberos principal to be used to connect to this Hbase source. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.hbase_source_registration_params import HbaseSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of HbaseSourceRegistrationParams from a JSON string
hbase_source_registration_params_instance = HbaseSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(HbaseSourceRegistrationParams.to_json())

# convert the object into a dict
hbase_source_registration_params_dict = hbase_source_registration_params_instance.to_dict()
# create an instance of HbaseSourceRegistrationParams from a dict
hbase_source_registration_params_from_dict = HbaseSourceRegistrationParams.from_dict(hbase_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


