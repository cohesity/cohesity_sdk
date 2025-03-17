# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.cassandra_params import CassandraParams
from cohesity_sdk.helios.models.couchbase_params import CouchbaseParams
from cohesity_sdk.helios.models.creation_info import CreationInfo
from cohesity_sdk.helios.models.hbase_params import HbaseParams
from cohesity_sdk.helios.models.hdfs_params import HdfsParams
from cohesity_sdk.helios.models.hive_params import HiveParams
from cohesity_sdk.helios.models.mongodb_params import MongodbParams
from cohesity_sdk.helios.models.recover_acropolis_params import RecoverAcropolisParams
from cohesity_sdk.helios.models.recover_aws_params import RecoverAwsParams
from cohesity_sdk.helios.models.recover_azure_params import RecoverAzureParams
from cohesity_sdk.helios.models.recover_elastifile_params import RecoverElastifileParams
from cohesity_sdk.helios.models.recover_exchange_params import RecoverExchangeParams
from cohesity_sdk.helios.models.recover_flashblade_params import RecoverFlashbladeParams
from cohesity_sdk.helios.models.recover_gcp_params import RecoverGcpParams
from cohesity_sdk.helios.models.recover_generic_nas_params import RecoverGenericNasParams
from cohesity_sdk.helios.models.recover_gpfs_params import RecoverGpfsParams
from cohesity_sdk.helios.models.recover_hyper_v_params import RecoverHyperVParams
from cohesity_sdk.helios.models.recover_isilon_params import RecoverIsilonParams
from cohesity_sdk.helios.models.recover_kubernetes_params import RecoverKubernetesParams
from cohesity_sdk.helios.models.recover_kvm_params import RecoverKvmParams
from cohesity_sdk.helios.models.recover_netapp_params import RecoverNetappParams
from cohesity_sdk.helios.models.recover_o365_params import RecoverO365Params
from cohesity_sdk.helios.models.recover_oracle_params import RecoverOracleParams
from cohesity_sdk.helios.models.recover_physical_params import RecoverPhysicalParams
from cohesity_sdk.helios.models.recover_pure_params import RecoverPureParams
from cohesity_sdk.helios.models.recover_salesforce_params import RecoverSalesforceParams
from cohesity_sdk.helios.models.recover_sql_params import RecoverSqlParams
from cohesity_sdk.helios.models.recover_view_params import RecoverViewParams
from cohesity_sdk.helios.models.recover_vmware_params import RecoverVmwareParams
from cohesity_sdk.helios.models.retrieve_archive_task import RetrieveArchiveTask
from cohesity_sdk.helios.models.tenant import Tenant
from cohesity_sdk.helios.models.uda_params import UdaParams
from typing import Set
from typing_extensions import Self

class Recovery(BaseModel):
    """
    Specifies a Recovery.
    """ # noqa: E501
    can_tear_down: Optional[StrictBool] = Field(default=None, description="Specifies whether it's possible to tear down the objects created by the recovery.", alias="canTearDown")
    creation_info: Optional[CreationInfo] = Field(default=None, alias="creationInfo")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of the Recovery in Unix timestamp epoch in microseconds. This field will be populated only after Recovery is finished.", alias="endTimeUsecs")
    id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specifies the id of the Recovery.")
    is_multi_stage_restore: Optional[StrictBool] = Field(default=None, description="Specifies whether the current recovery operation is a multi-stage restore operation. This is currently used by VMware recoveres for the migration/hot-standby use case.", alias="isMultiStageRestore")
    is_parent_recovery: Optional[StrictBool] = Field(default=None, description="Specifies whether the current recovery operation has created child recoveries. This is currently used in SQL recovery where multiple child recoveries can be tracked under a common/parent recovery.", alias="isParentRecovery")
    messages: Optional[List[StrictStr]] = Field(default=None, description="Specifies messages about the recovery.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Recovery.")
    parent_recovery_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="If current recovery is child recovery triggered by another parent recovery operation, then this field willt specify the id of the parent recovery.", alias="parentRecoveryId")
    permissions: Optional[List[Tenant]] = Field(default=None, description="Specifies the list of tenants that have permissions for this recovery.")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task id for Recovery.", alias="progressTaskId")
    recovery_action: Optional[StrictStr] = Field(default=None, description="Specifies the type of recover action.", alias="recoveryAction")
    retrieve_archive_tasks: Optional[List[RetrieveArchiveTask]] = Field(default=None, description="Specifies the list of persistent state of a retrieve of an archive task.", alias="retrieveArchiveTasks")
    snapshot_environment: Optional[StrictStr] = Field(default=None, description="Specifies the type of snapshot environment for which the Recovery was performed.", alias="snapshotEnvironment")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of the Recovery in Unix timestamp epoch in microseconds.", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Status of the Recovery. 'Running' indicates that the Recovery is still running. 'Canceled' indicates that the Recovery has been cancelled. 'Canceling' indicates that the Recovery is in the process of being cancelled. 'Failed' indicates that the Recovery has failed. 'Succeeded' indicates that the Recovery has finished successfully. 'SucceededWithWarning' indicates that the Recovery finished successfully, but there were some warning messages. 'Skipped' indicates that the Recovery task was skipped.")
    tear_down_message: Optional[StrictStr] = Field(default=None, description="Specifies the error message about the tear down operation if it fails.", alias="tearDownMessage")
    tear_down_status: Optional[StrictStr] = Field(default=None, description="Specifies the status of the tear down operation. This is only set when the canTearDown is set to true. 'DestroyScheduled' indicates that the tear down is ready to schedule. 'Destroying' indicates that the tear down is still running. 'Destroyed' indicates that the tear down succeeded. 'DestroyError' indicates that the tear down failed.", alias="tearDownStatus")
    acropolis_params: Optional[RecoverAcropolisParams] = Field(default=None, alias="acropolisParams")
    aws_params: Optional[RecoverAwsParams] = Field(default=None, alias="awsParams")
    azure_params: Optional[RecoverAzureParams] = Field(default=None, alias="azureParams")
    cassandra_params: Optional[CassandraParams] = Field(default=None, alias="cassandraParams")
    couchbase_params: Optional[CouchbaseParams] = Field(default=None, alias="couchbaseParams")
    elastifile_params: Optional[RecoverElastifileParams] = Field(default=None, alias="elastifileParams")
    exchange_params: Optional[RecoverExchangeParams] = Field(default=None, alias="exchangeParams")
    flashblade_params: Optional[RecoverFlashbladeParams] = Field(default=None, alias="flashbladeParams")
    gcp_params: Optional[RecoverGcpParams] = Field(default=None, alias="gcpParams")
    generic_nas_params: Optional[RecoverGenericNasParams] = Field(default=None, alias="genericNasParams")
    gpfs_params: Optional[RecoverGpfsParams] = Field(default=None, alias="gpfsParams")
    hbase_params: Optional[HbaseParams] = Field(default=None, alias="hbaseParams")
    hdfs_params: Optional[HdfsParams] = Field(default=None, alias="hdfsParams")
    hive_params: Optional[HiveParams] = Field(default=None, alias="hiveParams")
    hyperv_params: Optional[RecoverHyperVParams] = Field(default=None, alias="hypervParams")
    ibm_flash_system_params: Optional[RecoverPureParams] = Field(default=None, alias="ibmFlashSystemParams")
    isilon_params: Optional[RecoverIsilonParams] = Field(default=None, alias="isilonParams")
    kubernetes_params: Optional[RecoverKubernetesParams] = Field(default=None, alias="kubernetesParams")
    kvm_params: Optional[RecoverKvmParams] = Field(default=None, alias="kvmParams")
    mongodb_params: Optional[MongodbParams] = Field(default=None, alias="mongodbParams")
    mssql_params: Optional[RecoverSqlParams] = Field(default=None, alias="mssqlParams")
    netapp_params: Optional[RecoverNetappParams] = Field(default=None, alias="netappParams")
    office365_params: Optional[RecoverO365Params] = Field(default=None, alias="office365Params")
    oracle_params: Optional[RecoverOracleParams] = Field(default=None, alias="oracleParams")
    physical_params: Optional[RecoverPhysicalParams] = Field(default=None, alias="physicalParams")
    pure_params: Optional[RecoverPureParams] = Field(default=None, alias="pureParams")
    sfdc_params: Optional[RecoverSalesforceParams] = Field(default=None, alias="sfdcParams")
    uda_params: Optional[UdaParams] = Field(default=None, alias="udaParams")
    view_params: Optional[RecoverViewParams] = Field(default=None, alias="viewParams")
    vmware_params: Optional[RecoverVmwareParams] = Field(default=None, alias="vmwareParams")
    __properties: ClassVar[List[str]] = ["canTearDown", "creationInfo", "endTimeUsecs", "id", "isMultiStageRestore", "isParentRecovery", "messages", "name", "parentRecoveryId", "permissions", "progressTaskId", "recoveryAction", "retrieveArchiveTasks", "snapshotEnvironment", "startTimeUsecs", "status", "tearDownMessage", "tearDownStatus", "acropolisParams", "awsParams", "azureParams", "cassandraParams", "couchbaseParams", "elastifileParams", "exchangeParams", "flashbladeParams", "gcpParams", "genericNasParams", "gpfsParams", "hbaseParams", "hdfsParams", "hiveParams", "hypervParams", "ibmFlashSystemParams", "isilonParams", "kubernetesParams", "kvmParams", "mongodbParams", "mssqlParams", "netappParams", "office365Params", "oracleParams", "physicalParams", "pureParams", "sfdcParams", "udaParams", "viewParams", "vmwareParams"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+:\d+:\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+:\d+:\d+$/")
        return value

    @field_validator('parent_recovery_id')
    def parent_recovery_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+:\d+:\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+:\d+:\d+$/")
        return value

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RecoverVMs', 'RecoverFiles', 'InstantVolumeMount', 'RecoverVmDisks', 'RecoverVApps', 'RecoverVAppTemplates', 'UptierSnapshot', 'RecoverRDS', 'RecoverAurora', 'RecoverS3Buckets', 'RecoverRDSPostgres', 'RecoverAzureSQL', 'RecoverApps', 'CloneApps', 'RecoverNasVolume', 'RecoverPhysicalVolumes', 'RecoverSystem', 'RecoverExchangeDbs', 'CloneAppView', 'RecoverSanVolumes', 'RecoverSanGroup', 'RecoverMailbox', 'RecoverOneDrive', 'RecoverSharePoint', 'RecoverPublicFolders', 'RecoverMsGroup', 'RecoverMsTeam', 'ConvertToPst', 'DownloadChats', 'RecoverNamespaces', 'RecoverObjects', 'RecoverSfdcObjects', 'RecoverSfdcOrg', 'RecoverSfdcRecords', 'DownloadFilesAndFolders', 'CloneVMs', 'CloneView', 'CloneRefreshApp', 'CloneVMsToView', 'ConvertAndDeployVMs', 'DeployVMs']):
            raise ValueError("must be one of enum values ('RecoverVMs', 'RecoverFiles', 'InstantVolumeMount', 'RecoverVmDisks', 'RecoverVApps', 'RecoverVAppTemplates', 'UptierSnapshot', 'RecoverRDS', 'RecoverAurora', 'RecoverS3Buckets', 'RecoverRDSPostgres', 'RecoverAzureSQL', 'RecoverApps', 'CloneApps', 'RecoverNasVolume', 'RecoverPhysicalVolumes', 'RecoverSystem', 'RecoverExchangeDbs', 'CloneAppView', 'RecoverSanVolumes', 'RecoverSanGroup', 'RecoverMailbox', 'RecoverOneDrive', 'RecoverSharePoint', 'RecoverPublicFolders', 'RecoverMsGroup', 'RecoverMsTeam', 'ConvertToPst', 'DownloadChats', 'RecoverNamespaces', 'RecoverObjects', 'RecoverSfdcObjects', 'RecoverSfdcOrg', 'RecoverSfdcRecords', 'DownloadFilesAndFolders', 'CloneVMs', 'CloneView', 'CloneRefreshApp', 'CloneVMsToView', 'ConvertAndDeployVMs', 'DeployVMs')")
        return value

    @field_validator('snapshot_environment')
    def snapshot_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kPhysical', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kPhysical', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped']):
            raise ValueError("must be one of enum values ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped')")
        return value

    @field_validator('tear_down_status')
    def tear_down_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DestroyScheduled', 'Destroying', 'Destroyed', 'DestroyError']):
            raise ValueError("must be one of enum values ('DestroyScheduled', 'Destroying', 'Destroyed', 'DestroyError')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Recovery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of creation_info
        if self.creation_info:
            _dict['creationInfo'] = self.creation_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in retrieve_archive_tasks (list)
        _items = []
        if self.retrieve_archive_tasks:
            for _item_retrieve_archive_tasks in self.retrieve_archive_tasks:
                if _item_retrieve_archive_tasks:
                    _items.append(_item_retrieve_archive_tasks.to_dict())
            _dict['retrieveArchiveTasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of acropolis_params
        if self.acropolis_params:
            _dict['acropolisParams'] = self.acropolis_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_params
        if self.aws_params:
            _dict['awsParams'] = self.aws_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_params
        if self.azure_params:
            _dict['azureParams'] = self.azure_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cassandra_params
        if self.cassandra_params:
            _dict['cassandraParams'] = self.cassandra_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of couchbase_params
        if self.couchbase_params:
            _dict['couchbaseParams'] = self.couchbase_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of elastifile_params
        if self.elastifile_params:
            _dict['elastifileParams'] = self.elastifile_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exchange_params
        if self.exchange_params:
            _dict['exchangeParams'] = self.exchange_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flashblade_params
        if self.flashblade_params:
            _dict['flashbladeParams'] = self.flashblade_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_params
        if self.gcp_params:
            _dict['gcpParams'] = self.gcp_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generic_nas_params
        if self.generic_nas_params:
            _dict['genericNasParams'] = self.generic_nas_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpfs_params
        if self.gpfs_params:
            _dict['gpfsParams'] = self.gpfs_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hbase_params
        if self.hbase_params:
            _dict['hbaseParams'] = self.hbase_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hdfs_params
        if self.hdfs_params:
            _dict['hdfsParams'] = self.hdfs_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hive_params
        if self.hive_params:
            _dict['hiveParams'] = self.hive_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hyperv_params
        if self.hyperv_params:
            _dict['hypervParams'] = self.hyperv_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ibm_flash_system_params
        if self.ibm_flash_system_params:
            _dict['ibmFlashSystemParams'] = self.ibm_flash_system_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_params
        if self.isilon_params:
            _dict['isilonParams'] = self.isilon_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kubernetes_params
        if self.kubernetes_params:
            _dict['kubernetesParams'] = self.kubernetes_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kvm_params
        if self.kvm_params:
            _dict['kvmParams'] = self.kvm_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mongodb_params
        if self.mongodb_params:
            _dict['mongodbParams'] = self.mongodb_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mssql_params
        if self.mssql_params:
            _dict['mssqlParams'] = self.mssql_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_params
        if self.netapp_params:
            _dict['netappParams'] = self.netapp_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of office365_params
        if self.office365_params:
            _dict['office365Params'] = self.office365_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oracle_params
        if self.oracle_params:
            _dict['oracleParams'] = self.oracle_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of physical_params
        if self.physical_params:
            _dict['physicalParams'] = self.physical_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pure_params
        if self.pure_params:
            _dict['pureParams'] = self.pure_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfdc_params
        if self.sfdc_params:
            _dict['sfdcParams'] = self.sfdc_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uda_params
        if self.uda_params:
            _dict['udaParams'] = self.uda_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_params
        if self.view_params:
            _dict['viewParams'] = self.view_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vmware_params
        if self.vmware_params:
            _dict['vmwareParams'] = self.vmware_params.to_dict()
        # set to None if can_tear_down (nullable) is None
        # and model_fields_set contains the field
        if self.can_tear_down is None and "can_tear_down" in self.model_fields_set:
            _dict['canTearDown'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_multi_stage_restore (nullable) is None
        # and model_fields_set contains the field
        if self.is_multi_stage_restore is None and "is_multi_stage_restore" in self.model_fields_set:
            _dict['isMultiStageRestore'] = None

        # set to None if is_parent_recovery (nullable) is None
        # and model_fields_set contains the field
        if self.is_parent_recovery is None and "is_parent_recovery" in self.model_fields_set:
            _dict['isParentRecovery'] = None

        # set to None if messages (nullable) is None
        # and model_fields_set contains the field
        if self.messages is None and "messages" in self.model_fields_set:
            _dict['messages'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if parent_recovery_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_recovery_id is None and "parent_recovery_id" in self.model_fields_set:
            _dict['parentRecoveryId'] = None

        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

        # set to None if retrieve_archive_tasks (nullable) is None
        # and model_fields_set contains the field
        if self.retrieve_archive_tasks is None and "retrieve_archive_tasks" in self.model_fields_set:
            _dict['retrieveArchiveTasks'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if tear_down_message (nullable) is None
        # and model_fields_set contains the field
        if self.tear_down_message is None and "tear_down_message" in self.model_fields_set:
            _dict['tearDownMessage'] = None

        # set to None if tear_down_status (nullable) is None
        # and model_fields_set contains the field
        if self.tear_down_status is None and "tear_down_status" in self.model_fields_set:
            _dict['tearDownStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Recovery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canTearDown": obj.get("canTearDown"),
            "creationInfo": CreationInfo.from_dict(obj["creationInfo"]) if obj.get("creationInfo") is not None else None,
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "id": obj.get("id"),
            "isMultiStageRestore": obj.get("isMultiStageRestore"),
            "isParentRecovery": obj.get("isParentRecovery"),
            "messages": obj.get("messages"),
            "name": obj.get("name"),
            "parentRecoveryId": obj.get("parentRecoveryId"),
            "permissions": [Tenant.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "progressTaskId": obj.get("progressTaskId"),
            "recoveryAction": obj.get("recoveryAction"),
            "retrieveArchiveTasks": [RetrieveArchiveTask.from_dict(_item) for _item in obj["retrieveArchiveTasks"]] if obj.get("retrieveArchiveTasks") is not None else None,
            "snapshotEnvironment": obj.get("snapshotEnvironment"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status"),
            "tearDownMessage": obj.get("tearDownMessage"),
            "tearDownStatus": obj.get("tearDownStatus"),
            "acropolisParams": RecoverAcropolisParams.from_dict(obj["acropolisParams"]) if obj.get("acropolisParams") is not None else None,
            "awsParams": RecoverAwsParams.from_dict(obj["awsParams"]) if obj.get("awsParams") is not None else None,
            "azureParams": RecoverAzureParams.from_dict(obj["azureParams"]) if obj.get("azureParams") is not None else None,
            "cassandraParams": CassandraParams.from_dict(obj["cassandraParams"]) if obj.get("cassandraParams") is not None else None,
            "couchbaseParams": CouchbaseParams.from_dict(obj["couchbaseParams"]) if obj.get("couchbaseParams") is not None else None,
            "elastifileParams": RecoverElastifileParams.from_dict(obj["elastifileParams"]) if obj.get("elastifileParams") is not None else None,
            "exchangeParams": RecoverExchangeParams.from_dict(obj["exchangeParams"]) if obj.get("exchangeParams") is not None else None,
            "flashbladeParams": RecoverFlashbladeParams.from_dict(obj["flashbladeParams"]) if obj.get("flashbladeParams") is not None else None,
            "gcpParams": RecoverGcpParams.from_dict(obj["gcpParams"]) if obj.get("gcpParams") is not None else None,
            "genericNasParams": RecoverGenericNasParams.from_dict(obj["genericNasParams"]) if obj.get("genericNasParams") is not None else None,
            "gpfsParams": RecoverGpfsParams.from_dict(obj["gpfsParams"]) if obj.get("gpfsParams") is not None else None,
            "hbaseParams": HbaseParams.from_dict(obj["hbaseParams"]) if obj.get("hbaseParams") is not None else None,
            "hdfsParams": HdfsParams.from_dict(obj["hdfsParams"]) if obj.get("hdfsParams") is not None else None,
            "hiveParams": HiveParams.from_dict(obj["hiveParams"]) if obj.get("hiveParams") is not None else None,
            "hypervParams": RecoverHyperVParams.from_dict(obj["hypervParams"]) if obj.get("hypervParams") is not None else None,
            "ibmFlashSystemParams": RecoverPureParams.from_dict(obj["ibmFlashSystemParams"]) if obj.get("ibmFlashSystemParams") is not None else None,
            "isilonParams": RecoverIsilonParams.from_dict(obj["isilonParams"]) if obj.get("isilonParams") is not None else None,
            "kubernetesParams": RecoverKubernetesParams.from_dict(obj["kubernetesParams"]) if obj.get("kubernetesParams") is not None else None,
            "kvmParams": RecoverKvmParams.from_dict(obj["kvmParams"]) if obj.get("kvmParams") is not None else None,
            "mongodbParams": MongodbParams.from_dict(obj["mongodbParams"]) if obj.get("mongodbParams") is not None else None,
            "mssqlParams": RecoverSqlParams.from_dict(obj["mssqlParams"]) if obj.get("mssqlParams") is not None else None,
            "netappParams": RecoverNetappParams.from_dict(obj["netappParams"]) if obj.get("netappParams") is not None else None,
            "office365Params": RecoverO365Params.from_dict(obj["office365Params"]) if obj.get("office365Params") is not None else None,
            "oracleParams": RecoverOracleParams.from_dict(obj["oracleParams"]) if obj.get("oracleParams") is not None else None,
            "physicalParams": RecoverPhysicalParams.from_dict(obj["physicalParams"]) if obj.get("physicalParams") is not None else None,
            "pureParams": RecoverPureParams.from_dict(obj["pureParams"]) if obj.get("pureParams") is not None else None,
            "sfdcParams": RecoverSalesforceParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None,
            "udaParams": UdaParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None,
            "viewParams": RecoverViewParams.from_dict(obj["viewParams"]) if obj.get("viewParams") is not None else None,
            "vmwareParams": RecoverVmwareParams.from_dict(obj["vmwareParams"]) if obj.get("vmwareParams") is not None else None
        })
        return _obj


