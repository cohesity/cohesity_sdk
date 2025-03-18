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

class UpdateExistingArchivalSnapshotConfig(BaseModel):
    """
    Specifies the configuration about updating an existing Archival Snapshot Run.
    """ # noqa: E501
    archival_target_type: Optional[StrictStr] = Field(description="Specifies the snapshot's archival target type from which recovery has been performed.", alias="archivalTargetType")
    data_lock: Optional[StrictStr] = Field(default=None, description="Specifies WORM retention type for the snapshots. When a WORM retention type is specified, the snapshots of the Protection Groups using this policy will be kept until the maximum of the snapshot retention time. During that time, the snapshots cannot be deleted. <br>'Compliance' implies WORM retention is set for compliance reason. <br>'Administrative' implies WORM retention is set for administrative purposes.", alias="dataLock")
    days_to_keep: Optional[StrictInt] = Field(default=None, description="Specifies number of days to retain the snapshots. If positive, then this value is added to exisiting expiry time thereby increasing  the retention period of the snapshot. Conversly, if this value is negative, then value is subtracted to existing expiry time thereby decreasing the retention period of the snaphot. Here, by this operation if expiry time goes below current time then snapshot is immediately deleted.", alias="daysToKeep")
    delete_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies whether to delete the snapshot. When this is set to true, all other params will be ignored.", alias="deleteSnapshot")
    enable_legal_hold: Optional[StrictBool] = Field(default=None, description="Specifies whether to retain the snapshot for legal purpose. If set to true, the snapshots cannot be deleted until the retention period. Note that using this option may cause the Cluster to run out of space. If set to false explicitly, the hold is removed, and the snapshots will expire as specified in the policy of the Protection Group. If this field is not specified, there is no change to the hold of the run. This field can be set only by a User having Data Security Role.", alias="enableLegalHold")
    id: StrictInt = Field(description="Specifies the id of the archival target.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the archival target.")
    resync: Optional[StrictBool] = Field(default=None, description="Specifies whether to retry the archival operation in case if earlier attempt failed. If not specified or set to false, archival is not retried.")
    __properties: ClassVar[List[str]] = ["archivalTargetType", "dataLock", "daysToKeep", "deleteSnapshot", "enableLegalHold", "id", "name", "resync"]

    @field_validator('archival_target_type')
    def archival_target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Tape', 'Cloud', 'Nas']):
            raise ValueError("must be one of enum values ('Tape', 'Cloud', 'Nas')")
        return value

    @field_validator('data_lock')
    def data_lock_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Compliance', 'Administrative']):
            raise ValueError("must be one of enum values ('Compliance', 'Administrative')")
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
        """Create an instance of UpdateExistingArchivalSnapshotConfig from a JSON string"""
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
        # set to None if archival_target_type (nullable) is None
        # and model_fields_set contains the field
        if self.archival_target_type is None and "archival_target_type" in self.model_fields_set:
            _dict['archivalTargetType'] = None

        # set to None if data_lock (nullable) is None
        # and model_fields_set contains the field
        if self.data_lock is None and "data_lock" in self.model_fields_set:
            _dict['dataLock'] = None

        # set to None if days_to_keep (nullable) is None
        # and model_fields_set contains the field
        if self.days_to_keep is None and "days_to_keep" in self.model_fields_set:
            _dict['daysToKeep'] = None

        # set to None if delete_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.delete_snapshot is None and "delete_snapshot" in self.model_fields_set:
            _dict['deleteSnapshot'] = None

        # set to None if enable_legal_hold (nullable) is None
        # and model_fields_set contains the field
        if self.enable_legal_hold is None and "enable_legal_hold" in self.model_fields_set:
            _dict['enableLegalHold'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if resync (nullable) is None
        # and model_fields_set contains the field
        if self.resync is None and "resync" in self.model_fields_set:
            _dict['resync'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateExistingArchivalSnapshotConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTargetType": obj.get("archivalTargetType"),
            "dataLock": obj.get("dataLock"),
            "daysToKeep": obj.get("daysToKeep"),
            "deleteSnapshot": obj.get("deleteSnapshot"),
            "enableLegalHold": obj.get("enableLegalHold"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "resync": obj.get("resync")
        })
        return _obj


