# RecoverAzureParams

Specifies the recovery options specific to Azure environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**azure_blob_storage_params** | [**RecoverAzureBlobStorageParams**](RecoverAzureBlobStorageParams.md) |  | [optional] 
**azure_cosmos_db_cassandra_params** | [**RecoverAzureCosmosDBCassandraParams**](RecoverAzureCosmosDBCassandraParams.md) |  | [optional] 
**azure_cosmos_db_mongo_db_params** | [**RecoverAzureCosmosDBMongoDBParams**](RecoverAzureCosmosDBMongoDBParams.md) |  | [optional] 
**azure_cosmos_dbno_sql_params** | [**RecoverAzureCosmosDBNoSQLParams**](RecoverAzureCosmosDBNoSQLParams.md) |  | [optional] 
**azure_entra_id_params** | [**RecoverAzureEntraIdParams**](RecoverAzureEntraIdParams.md) |  | [optional] 
**azure_mysql_params** | [**RecoverAzureMySQLParams**](RecoverAzureMySQLParams.md) |  | [optional] 
**azure_postgre_sql_params** | [**RecoverAzurePostgreSQLParams**](RecoverAzurePostgreSQLParams.md) |  | [optional] 
**azure_sqldb_params** | [**RecoverAzureSQLDBParams**](RecoverAzureSQLDBParams.md) |  | [optional] 
**azure_sqlmi_params** | [**RecoverAzureSQLMIParams**](RecoverAzureSQLMIParams.md) |  | [optional] 
**azure_sql_params** | [**RecoverAzureSqlParams**](RecoverAzureSqlParams.md) |  | [optional] 
**azure_table_api_params** | [**RecoverAzureTableAPIParams**](RecoverAzureTableAPIParams.md) |  | [optional] 
**azure_table_storage_params** | [**RecoverAzureTableStorageParams**](RecoverAzureTableStorageParams.md) |  | [optional] 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_file_and_folder_params** | [**RecoverAzureFileAndFolderParams**](RecoverAzureFileAndFolderParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverAzureVmParams**](RecoverAzureVmParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


