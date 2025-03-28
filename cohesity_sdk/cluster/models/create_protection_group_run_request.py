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
from cohesity_sdk.cluster.models.cassandra_protection_run_params import CassandraProtectionRunParams
from cohesity_sdk.cluster.models.run_object import RunObject
from cohesity_sdk.cluster.models.run_targets_configuration import RunTargetsConfiguration
from cohesity_sdk.cluster.models.uda_protection_run_params import UdaProtectionRunParams
from typing import Set
from typing_extensions import Self

class CreateProtectionGroupRunRequest(BaseModel):
    """
    Specifies the request to create a protection run. On success, the system will accept the request and return the Protection Group id for which the run is supposed to start. The actual run may start at a later time if the system is busy. Consumers must query the Protection Group to see the run.
    """ # noqa: E501
    cassandra_params: Optional[CassandraProtectionRunParams] = Field(default=None, alias="cassandraParams")
    objects: Optional[List[RunObject]] = Field(default=None, description="Specifies the list of objects to be protected by this Protection Group run. These can be leaf objects or non-leaf objects in the protection hierarchy. This must be specified only if a subset of objects from the Protection Groups needs to be protected.")
    run_type: Optional[StrictStr] = Field(description="Type of protection run. 'kRegular' indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. 'kFull' indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. 'kLog' indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. 'kSystem' indicates system volume backup. It produces an image for bare metal recovery.", alias="runType")
    targets_config: Optional[RunTargetsConfiguration] = Field(default=None, alias="targetsConfig")
    uda_params: Optional[UdaProtectionRunParams] = Field(default=None, alias="udaParams")
    __properties: ClassVar[List[str]] = ["cassandraParams", "objects", "runType", "targetsConfig", "udaParams"]

    @field_validator('run_type')
    def run_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot']):
            raise ValueError("must be one of enum values ('kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot')")
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
        """Create an instance of CreateProtectionGroupRunRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cassandra_params
        if self.cassandra_params:
            _dict['cassandraParams'] = self.cassandra_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of targets_config
        if self.targets_config:
            _dict['targetsConfig'] = self.targets_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uda_params
        if self.uda_params:
            _dict['udaParams'] = self.uda_params.to_dict()
        # set to None if run_type (nullable) is None
        # and model_fields_set contains the field
        if self.run_type is None and "run_type" in self.model_fields_set:
            _dict['runType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateProtectionGroupRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cassandraParams": CassandraProtectionRunParams.from_dict(obj["cassandraParams"]) if obj.get("cassandraParams") is not None else None,
            "objects": [RunObject.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "runType": obj.get("runType"),
            "targetsConfig": RunTargetsConfiguration.from_dict(obj["targetsConfig"]) if obj.get("targetsConfig") is not None else None,
            "udaParams": UdaProtectionRunParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None
        })
        return _obj


