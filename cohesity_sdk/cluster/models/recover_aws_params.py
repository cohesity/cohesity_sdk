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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.common_download_file_and_folder_params import CommonDownloadFileAndFolderParams
from cohesity_sdk.cluster.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.cluster.models.recover_aws_aurora_params import RecoverAwsAuroraParams
from cohesity_sdk.cluster.models.recover_aws_file_and_folder_params import RecoverAwsFileAndFolderParams
from cohesity_sdk.cluster.models.recover_aws_rds_params import RecoverAwsRdsParams
from cohesity_sdk.cluster.models.recover_aws_s3_bucket_params import RecoverAwsS3BucketParams
from cohesity_sdk.cluster.models.recover_aws_vm_params import RecoverAwsVmParams
from cohesity_sdk.cluster.models.recover_rds_postgres_params import RecoverRDSPostgresParams
from typing import Optional, Set
from typing_extensions import Self

class RecoverAwsParams(BaseModel):
    """
    Specifies the recovery options specific to AWS environment.
    """ # noqa: E501
    download_file_and_folder_params: Optional[CommonDownloadFileAndFolderParams] = Field(default=None, alias="downloadFileAndFolderParams")
    objects: Optional[List[CommonRecoverObjectSnapshotParams]] = Field(default=None, description="Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM's or a Protection Group Run details to recover all the VM's that are backed up by that Run. For recovering files, specifies the object contains the file to recover.")
    recover_aurora_params: Optional[RecoverAwsAuroraParams] = Field(default=None, alias="recoverAuroraParams")
    recover_file_and_folder_params: Optional[RecoverAwsFileAndFolderParams] = Field(default=None, alias="recoverFileAndFolderParams")
    recover_rds_ingest_params: Optional[RecoverRDSPostgresParams] = Field(default=None, alias="recoverRdsIngestParams")
    recover_rds_params: Optional[RecoverAwsRdsParams] = Field(default=None, alias="recoverRdsParams")
    recover_s3_bucket_params: Optional[RecoverAwsS3BucketParams] = Field(default=None, alias="recoverS3BucketParams")
    recover_vm_params: Optional[RecoverAwsVmParams] = Field(default=None, alias="recoverVmParams")
    recovery_action: StrictStr = Field(description="Specifies the type of recover action to be performed.", alias="recoveryAction")
    __properties: ClassVar[List[str]] = ["downloadFileAndFolderParams", "objects", "recoverAuroraParams", "recoverFileAndFolderParams", "recoverRdsIngestParams", "recoverRdsParams", "recoverS3BucketParams", "recoverVmParams", "recoveryAction"]

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RecoverVMs', 'RecoverRDS', 'RecoverAurora', 'RecoverFiles', 'RecoverS3Buckets', 'RecoverRDSPostgres']):
            raise ValueError("must be one of enum values ('RecoverVMs', 'RecoverRDS', 'RecoverAurora', 'RecoverFiles', 'RecoverS3Buckets', 'RecoverRDSPostgres')")
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
        """Create an instance of RecoverAwsParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of download_file_and_folder_params
        if self.download_file_and_folder_params:
            _dict['downloadFileAndFolderParams'] = self.download_file_and_folder_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of recover_aurora_params
        if self.recover_aurora_params:
            _dict['recoverAuroraParams'] = self.recover_aurora_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_file_and_folder_params
        if self.recover_file_and_folder_params:
            _dict['recoverFileAndFolderParams'] = self.recover_file_and_folder_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_rds_ingest_params
        if self.recover_rds_ingest_params:
            _dict['recoverRdsIngestParams'] = self.recover_rds_ingest_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_rds_params
        if self.recover_rds_params:
            _dict['recoverRdsParams'] = self.recover_rds_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_s3_bucket_params
        if self.recover_s3_bucket_params:
            _dict['recoverS3BucketParams'] = self.recover_s3_bucket_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_vm_params
        if self.recover_vm_params:
            _dict['recoverVmParams'] = self.recover_vm_params.to_dict()
        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverAwsParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "downloadFileAndFolderParams": CommonDownloadFileAndFolderParams.from_dict(obj["downloadFileAndFolderParams"]) if obj.get("downloadFileAndFolderParams") is not None else None,
            "objects": [CommonRecoverObjectSnapshotParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "recoverAuroraParams": RecoverAwsAuroraParams.from_dict(obj["recoverAuroraParams"]) if obj.get("recoverAuroraParams") is not None else None,
            "recoverFileAndFolderParams": RecoverAwsFileAndFolderParams.from_dict(obj["recoverFileAndFolderParams"]) if obj.get("recoverFileAndFolderParams") is not None else None,
            "recoverRdsIngestParams": RecoverRDSPostgresParams.from_dict(obj["recoverRdsIngestParams"]) if obj.get("recoverRdsIngestParams") is not None else None,
            "recoverRdsParams": RecoverAwsRdsParams.from_dict(obj["recoverRdsParams"]) if obj.get("recoverRdsParams") is not None else None,
            "recoverS3BucketParams": RecoverAwsS3BucketParams.from_dict(obj["recoverS3BucketParams"]) if obj.get("recoverS3BucketParams") is not None else None,
            "recoverVmParams": RecoverAwsVmParams.from_dict(obj["recoverVmParams"]) if obj.get("recoverVmParams") is not None else None,
            "recoveryAction": obj.get("recoveryAction")
        })
        return _obj


