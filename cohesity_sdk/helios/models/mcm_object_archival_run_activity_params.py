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
from typing import Set
from typing_extensions import Self

class McmObjectArchivalRunActivityParams(BaseModel):
    """
    Specifies the Object activity of an archival run.
    """ # noqa: E501
    archival_target_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of archival target.", alias="archivalTargetId")
    archival_target_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of archival target.", alias="archivalTargetName")
    bytes_read: Optional[StrictInt] = Field(default=None, description="Specifies total logical bytes read for creating the snapshot.", alias="bytesRead")
    bytes_written: Optional[StrictInt] = Field(default=None, description="Specifies total size of data in bytes written after taking backup.", alias="bytesWritten")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of Run in Unix epoch Timestamp(in microseconds).", alias="endTimeUsecs")
    error_message: Optional[StrictStr] = Field(default=None, description="Specifies the full text of the error message if any error occurs.", alias="errorMessage")
    is_cloud_archival_direct: Optional[StrictBool] = Field(default=None, description="Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location.", alias="isCloudArchivalDirect")
    is_sla_violated: Optional[StrictBool] = Field(default=None, description="Indicated if SLA has been violated for this run.", alias="isSlaViolated")
    is_stubbed_run: Optional[StrictBool] = Field(default=None, description="Specifies whether this is a stubbed run. This is set by the server and if set to true, this run entry specifies the user intent to create a run instead of actual run itself", alias="isStubbedRun")
    logical_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies total logical size of the object in bytes.", alias="logicalSizeBytes")
    message_code: Optional[StrictStr] = Field(default=None, description="Specifies a short message describing the type of error which occurred.", alias="messageCode")
    message_guid: Optional[StrictStr] = Field(default=None, description="Specifies the identifier of the error code.", alias="messageGuid")
    policy_id: Optional[StrictStr] = Field(default=None, description="Specifies the Protection Policy Id.", alias="policyId")
    policy_name: Optional[StrictStr] = Field(default=None, description="Specifies the Protection Policy Name.", alias="policyName")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task id for the Run.", alias="progressTaskId")
    protection_environment_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of protection environment.", alias="protectionEnvironmentType")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the Protection Group Id.", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="Specifies the Protection Group name.", alias="protectionGroupName")
    run_id: Optional[StrictStr] = Field(default=None, description="Specifies the ID of the Protection Run.", alias="runId")
    run_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the Protection Run.", alias="runType")
    snapshot_id: Optional[StrictStr] = Field(default=None, description="Specifies the id of the object snapshot that is created as a part of this Run. This field is only populated for runs which are successful.", alias="snapshotId")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of Run in Unix epoch Timestamp(in microseconds).", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Status of the Run. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. 'Skipped' indicates that the run was skipped.")
    __properties: ClassVar[List[str]] = ["archivalTargetId", "archivalTargetName", "bytesRead", "bytesWritten", "endTimeUsecs", "errorMessage", "isCloudArchivalDirect", "isSlaViolated", "isStubbedRun", "logicalSizeBytes", "messageCode", "messageGuid", "policyId", "policyName", "progressTaskId", "protectionEnvironmentType", "protectionGroupId", "protectionGroupName", "runId", "runType", "snapshotId", "startTimeUsecs", "status"]

    @field_validator('protection_environment_type')
    def protection_environment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('run_type')
    def run_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot']):
            raise ValueError("must be one of enum values ('kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped']):
            raise ValueError("must be one of enum values ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped')")
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
        """Create an instance of McmObjectArchivalRunActivityParams from a JSON string"""
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
        # set to None if archival_target_id (nullable) is None
        # and model_fields_set contains the field
        if self.archival_target_id is None and "archival_target_id" in self.model_fields_set:
            _dict['archivalTargetId'] = None

        # set to None if archival_target_name (nullable) is None
        # and model_fields_set contains the field
        if self.archival_target_name is None and "archival_target_name" in self.model_fields_set:
            _dict['archivalTargetName'] = None

        # set to None if bytes_read (nullable) is None
        # and model_fields_set contains the field
        if self.bytes_read is None and "bytes_read" in self.model_fields_set:
            _dict['bytesRead'] = None

        # set to None if bytes_written (nullable) is None
        # and model_fields_set contains the field
        if self.bytes_written is None and "bytes_written" in self.model_fields_set:
            _dict['bytesWritten'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if is_cloud_archival_direct (nullable) is None
        # and model_fields_set contains the field
        if self.is_cloud_archival_direct is None and "is_cloud_archival_direct" in self.model_fields_set:
            _dict['isCloudArchivalDirect'] = None

        # set to None if is_sla_violated (nullable) is None
        # and model_fields_set contains the field
        if self.is_sla_violated is None and "is_sla_violated" in self.model_fields_set:
            _dict['isSlaViolated'] = None

        # set to None if is_stubbed_run (nullable) is None
        # and model_fields_set contains the field
        if self.is_stubbed_run is None and "is_stubbed_run" in self.model_fields_set:
            _dict['isStubbedRun'] = None

        # set to None if logical_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.logical_size_bytes is None and "logical_size_bytes" in self.model_fields_set:
            _dict['logicalSizeBytes'] = None

        # set to None if message_code (nullable) is None
        # and model_fields_set contains the field
        if self.message_code is None and "message_code" in self.model_fields_set:
            _dict['messageCode'] = None

        # set to None if message_guid (nullable) is None
        # and model_fields_set contains the field
        if self.message_guid is None and "message_guid" in self.model_fields_set:
            _dict['messageGuid'] = None

        # set to None if policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.policy_id is None and "policy_id" in self.model_fields_set:
            _dict['policyId'] = None

        # set to None if policy_name (nullable) is None
        # and model_fields_set contains the field
        if self.policy_name is None and "policy_name" in self.model_fields_set:
            _dict['policyName'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

        # set to None if protection_environment_type (nullable) is None
        # and model_fields_set contains the field
        if self.protection_environment_type is None and "protection_environment_type" in self.model_fields_set:
            _dict['protectionEnvironmentType'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if run_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_id is None and "run_id" in self.model_fields_set:
            _dict['runId'] = None

        # set to None if run_type (nullable) is None
        # and model_fields_set contains the field
        if self.run_type is None and "run_type" in self.model_fields_set:
            _dict['runType'] = None

        # set to None if snapshot_id (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_id is None and "snapshot_id" in self.model_fields_set:
            _dict['snapshotId'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of McmObjectArchivalRunActivityParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTargetId": obj.get("archivalTargetId"),
            "archivalTargetName": obj.get("archivalTargetName"),
            "bytesRead": obj.get("bytesRead"),
            "bytesWritten": obj.get("bytesWritten"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "errorMessage": obj.get("errorMessage"),
            "isCloudArchivalDirect": obj.get("isCloudArchivalDirect"),
            "isSlaViolated": obj.get("isSlaViolated"),
            "isStubbedRun": obj.get("isStubbedRun"),
            "logicalSizeBytes": obj.get("logicalSizeBytes"),
            "messageCode": obj.get("messageCode"),
            "messageGuid": obj.get("messageGuid"),
            "policyId": obj.get("policyId"),
            "policyName": obj.get("policyName"),
            "progressTaskId": obj.get("progressTaskId"),
            "protectionEnvironmentType": obj.get("protectionEnvironmentType"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "runId": obj.get("runId"),
            "runType": obj.get("runType"),
            "snapshotId": obj.get("snapshotId"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status")
        })
        return _obj


