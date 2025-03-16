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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.cluster.models.externally_triggered_job_params import ExternallyTriggeredJobParams
from cohesity_sdk.cluster.models.indexing_policy import IndexingPolicy
from cohesity_sdk.cluster.models.view_protection_group_object_params import ViewProtectionGroupObjectParams
from cohesity_sdk.cluster.models.view_protection_group_replication_params import ViewProtectionGroupReplicationParams
from typing import Optional, Set
from typing_extensions import Self

class ViewProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to view related Protection Groups.
    """ # noqa: E501
    externally_triggered_job_params: Optional[ExternallyTriggeredJobParams] = Field(default=None, alias="externallyTriggeredJobParams")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    objects: Annotated[List[ViewProtectionGroupObjectParams], Field(min_length=1)] = Field(description="Specifies the objects to be included in the Protection Group.")
    replication_params: Optional[ViewProtectionGroupReplicationParams] = Field(default=None, alias="replicationParams")
    __properties: ClassVar[List[str]] = ["externallyTriggeredJobParams", "indexingPolicy", "objects", "replicationParams"]

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
        """Create an instance of ViewProtectionGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of externally_triggered_job_params
        if self.externally_triggered_job_params:
            _dict['externallyTriggeredJobParams'] = self.externally_triggered_job_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of replication_params
        if self.replication_params:
            _dict['replicationParams'] = self.replication_params.to_dict()
        # set to None if replication_params (nullable) is None
        # and model_fields_set contains the field
        if self.replication_params is None and "replication_params" in self.model_fields_set:
            _dict['replicationParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "externallyTriggeredJobParams": ExternallyTriggeredJobParams.from_dict(obj["externallyTriggeredJobParams"]) if obj.get("externallyTriggeredJobParams") is not None else None,
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None,
            "objects": [ViewProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "replicationParams": ViewProtectionGroupReplicationParams.from_dict(obj["replicationParams"]) if obj.get("replicationParams") is not None else None
        })
        return _obj


