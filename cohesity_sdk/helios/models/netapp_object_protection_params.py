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
from cohesity_sdk.helios.models.continuous_snapshot_params import ContinuousSnapshotParams
from cohesity_sdk.helios.models.snapshot_label import SnapshotLabel
from typing import Optional, Set
from typing_extensions import Self

class NetappObjectProtectionParams(BaseModel):
    """
    Specifies the parameters which are specific to Netapp object protection.
    """ # noqa: E501
    backup_existing_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies that snapshot label is not set for Data-Protect Netapp Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false.", alias="backupExistingSnapshot")
    continuous_snapshots: Optional[ContinuousSnapshotParams] = Field(default=None, alias="continuousSnapshots")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection.", alias="excludeObjectIds")
    protocol: Optional[StrictStr] = Field(default=None, description="Specifies the protocol of the NAS device being backed up.")
    snapshot_label: Optional[SnapshotLabel] = Field(default=None, alias="snapshotLabel")
    __properties: ClassVar[List[str]] = ["backupExistingSnapshot", "continuousSnapshots", "excludeObjectIds", "protocol", "snapshotLabel"]

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3']):
            raise ValueError("must be one of enum values ('kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3')")
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
        """Create an instance of NetappObjectProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of continuous_snapshots
        if self.continuous_snapshots:
            _dict['continuousSnapshots'] = self.continuous_snapshots.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_label
        if self.snapshot_label:
            _dict['snapshotLabel'] = self.snapshot_label.to_dict()
        # set to None if backup_existing_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.backup_existing_snapshot is None and "backup_existing_snapshot" in self.model_fields_set:
            _dict['backupExistingSnapshot'] = None

        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetappObjectProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupExistingSnapshot": obj.get("backupExistingSnapshot"),
            "continuousSnapshots": ContinuousSnapshotParams.from_dict(obj["continuousSnapshots"]) if obj.get("continuousSnapshots") is not None else None,
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "protocol": obj.get("protocol"),
            "snapshotLabel": SnapshotLabel.from_dict(obj["snapshotLabel"]) if obj.get("snapshotLabel") is not None else None
        })
        return _obj


