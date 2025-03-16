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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.key_value_pair import KeyValuePair
from cohesity_sdk.helios.models.uda_protection_group_object_params import UdaProtectionGroupObjectParams
from typing import Optional, Set
from typing_extensions import Self

class UdaProtectionGroupParams(BaseModel):
    """
    Specifies parameters related to the Universal Data Adapter Protection job.
    """ # noqa: E501
    backup_job_arguments: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the map of custom arguments to be supplied to the various backup scripts.", alias="backupJobArguments")
    concurrency: Optional[StrictInt] = Field(default=1, description="Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1.")
    et_log_backup: Optional[StrictBool] = Field(default=None, description="Specifies whether this Protection Group is created from a source having externally triggered log backup support.", alias="etLogBackup")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    full_backup_args: Optional[StrictStr] = Field(default=None, description="Specifies the custom arguments to be supplied to the full backup script when a full backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead.", alias="fullBackupArgs")
    has_entity_support: Optional[StrictBool] = Field(default=None, description="Specifies whether this Protection Group is created from a source having entity support.", alias="hasEntitySupport")
    incr_backup_args: Optional[StrictStr] = Field(default=None, description="Specifies the custom arguments to be supplied to the incremental backup script when an incremental backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead.", alias="incrBackupArgs")
    log_backup_args: Optional[StrictStr] = Field(default=None, description="Specifies the custom arguments to be supplied to the log backup script when a log backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead.", alias="logBackupArgs")
    mounts: Optional[StrictInt] = Field(default=1, description="Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1.")
    objects: Annotated[List[UdaProtectionGroupObjectParams], Field(min_length=1)] = Field(description="Specifies a list of fully qualified names of the objects to be protected.")
    source_id: Optional[StrictInt] = Field(description="Specifies the source Id of the objects to be protected.", alias="sourceId")
    __properties: ClassVar[List[str]] = ["backupJobArguments", "concurrency", "etLogBackup", "excludeObjectIds", "fullBackupArgs", "hasEntitySupport", "incrBackupArgs", "logBackupArgs", "mounts", "objects", "sourceId"]

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
        """Create an instance of UdaProtectionGroupParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "et_log_backup",
            "has_entity_support",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in backup_job_arguments (list)
        _items = []
        if self.backup_job_arguments:
            for _item_backup_job_arguments in self.backup_job_arguments:
                if _item_backup_job_arguments:
                    _items.append(_item_backup_job_arguments.to_dict())
            _dict['backupJobArguments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if backup_job_arguments (nullable) is None
        # and model_fields_set contains the field
        if self.backup_job_arguments is None and "backup_job_arguments" in self.model_fields_set:
            _dict['backupJobArguments'] = None

        # set to None if concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.concurrency is None and "concurrency" in self.model_fields_set:
            _dict['concurrency'] = None

        # set to None if et_log_backup (nullable) is None
        # and model_fields_set contains the field
        if self.et_log_backup is None and "et_log_backup" in self.model_fields_set:
            _dict['etLogBackup'] = None

        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if full_backup_args (nullable) is None
        # and model_fields_set contains the field
        if self.full_backup_args is None and "full_backup_args" in self.model_fields_set:
            _dict['fullBackupArgs'] = None

        # set to None if has_entity_support (nullable) is None
        # and model_fields_set contains the field
        if self.has_entity_support is None and "has_entity_support" in self.model_fields_set:
            _dict['hasEntitySupport'] = None

        # set to None if incr_backup_args (nullable) is None
        # and model_fields_set contains the field
        if self.incr_backup_args is None and "incr_backup_args" in self.model_fields_set:
            _dict['incrBackupArgs'] = None

        # set to None if log_backup_args (nullable) is None
        # and model_fields_set contains the field
        if self.log_backup_args is None and "log_backup_args" in self.model_fields_set:
            _dict['logBackupArgs'] = None

        # set to None if mounts (nullable) is None
        # and model_fields_set contains the field
        if self.mounts is None and "mounts" in self.model_fields_set:
            _dict['mounts'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UdaProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupJobArguments": [KeyValuePair.from_dict(_item) for _item in obj["backupJobArguments"]] if obj.get("backupJobArguments") is not None else None,
            "concurrency": obj.get("concurrency") if obj.get("concurrency") is not None else 1,
            "etLogBackup": obj.get("etLogBackup"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "fullBackupArgs": obj.get("fullBackupArgs"),
            "hasEntitySupport": obj.get("hasEntitySupport"),
            "incrBackupArgs": obj.get("incrBackupArgs"),
            "logBackupArgs": obj.get("logBackupArgs"),
            "mounts": obj.get("mounts") if obj.get("mounts") is not None else 1,
            "objects": [UdaProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "sourceId": obj.get("sourceId")
        })
        return _obj


