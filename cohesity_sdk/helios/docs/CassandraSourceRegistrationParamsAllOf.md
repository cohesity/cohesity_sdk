# CassandraSourceRegistrationParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jmx_credentials** | [**CassandraSourceRegistrationParamsAllOfJmxCredentials**](CassandraSourceRegistrationParamsAllOfJmxCredentials.md) |  | [optional] 
**cassandra_credentials** | [**CassandraSourceRegistrationParamsAllOfCassandraCredentials**](CassandraSourceRegistrationParamsAllOfCassandraCredentials.md) |  | [optional] 
**data_center_names** | **[str]** | Data centers for this cluster. | [optional] 
**kerberos_principal** | **str, none_type** | Principal for the kerberos connection. (This is required only if your Cassandra has Kerberos authentication. Please refer to the user guide.) | [optional] 
**dse_solr_info** | [**DSESolrInfo**](DSESolrInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


