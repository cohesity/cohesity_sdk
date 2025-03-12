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
from cohesity_sdk.helios.models.failover_source_cluster import FailoverSourceCluster
from cohesity_sdk.helios.models.source_replica_object import SourceReplicaObject
from typing import Optional, Set
from typing_extensions import Self

class InitFailoverResponse(BaseModel):
    """
    Specifies the response after succesfully initiating the failover request.
    """ # noqa: E501
    replica_to_source_objects: Optional[List[SourceReplicaObject]] = Field(default=None, description="Specifies the list of corrosponding source objects mapped with replica objects provided at the time of initiating failover request.", alias="replicaToSourceObjects")
    source_cluster_info: Optional[FailoverSourceCluster] = Field(default=None, alias="sourceClusterInfo")
    __properties: ClassVar[List[str]] = ["replicaToSourceObjects", "sourceClusterInfo"]

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
        """Create an instance of InitFailoverResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in replica_to_source_objects (list)
        _items = []
        if self.replica_to_source_objects:
            for _item_replica_to_source_objects in self.replica_to_source_objects:
                if _item_replica_to_source_objects:
                    _items.append(_item_replica_to_source_objects.to_dict())
            _dict['replicaToSourceObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of source_cluster_info
        if self.source_cluster_info:
            _dict['sourceClusterInfo'] = self.source_cluster_info.to_dict()
        # set to None if replica_to_source_objects (nullable) is None
        # and model_fields_set contains the field
        if self.replica_to_source_objects is None and "replica_to_source_objects" in self.model_fields_set:
            _dict['replicaToSourceObjects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InitFailoverResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "replicaToSourceObjects": [SourceReplicaObject.from_dict(_item) for _item in obj["replicaToSourceObjects"]] if obj.get("replicaToSourceObjects") is not None else None,
            "sourceClusterInfo": FailoverSourceCluster.from_dict(obj["sourceClusterInfo"]) if obj.get("sourceClusterInfo") is not None else None
        })
        return _obj


