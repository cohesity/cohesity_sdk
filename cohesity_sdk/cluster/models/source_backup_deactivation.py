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
from cohesity_sdk.cluster.models.failover_object import FailoverObject
from typing import Set
from typing_extensions import Self

class SourceBackupDeactivation(BaseModel):
    """
    Specifies the request parmeters to deactivate the backup of failover entities on source cluster.
    """ # noqa: E501
    keep_failover_objects: Optional[StrictBool] = Field(default=None, description="If this is set to true then objects will not be removed from protection group. If this is set to false, then all objects which are being failed over will be removed from the protection group. If protection group left with zero entities then it will be paused automatically.", alias="keepFailoverObjects")
    objects: Optional[List[FailoverObject]] = Field(default=None, description="Specifies the list of all local entity ids of all the objects being failed from the source cluster. Backup will be deactiaved for all given objects.")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the protection group id of the source cluster from where the objects being failed over. If this is not specified then it will be infer from the list of objects being failed over.", alias="protectionGroupId")
    replication_cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the replication cluster Id involved in failover operation.", alias="replicationClusterId")
    view_id: Optional[StrictStr] = Field(default=None, description="If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over. Backup will be deactivated for view object.", alias="viewId")
    __properties: ClassVar[List[str]] = ["keepFailoverObjects", "objects", "protectionGroupId", "replicationClusterId", "viewId"]

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
        """Create an instance of SourceBackupDeactivation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "view_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if keep_failover_objects (nullable) is None
        # and model_fields_set contains the field
        if self.keep_failover_objects is None and "keep_failover_objects" in self.model_fields_set:
            _dict['keepFailoverObjects'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if replication_cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.replication_cluster_id is None and "replication_cluster_id" in self.model_fields_set:
            _dict['replicationClusterId'] = None

        # set to None if view_id (nullable) is None
        # and model_fields_set contains the field
        if self.view_id is None and "view_id" in self.model_fields_set:
            _dict['viewId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceBackupDeactivation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keepFailoverObjects": obj.get("keepFailoverObjects"),
            "objects": [FailoverObject.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "protectionGroupId": obj.get("protectionGroupId"),
            "replicationClusterId": obj.get("replicationClusterId"),
            "viewId": obj.get("viewId")
        })
        return _obj


