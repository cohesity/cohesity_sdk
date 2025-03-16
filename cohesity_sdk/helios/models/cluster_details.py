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
from cohesity_sdk.helios.models.cluster_info import ClusterInfo
from cohesity_sdk.helios.models.sp_cluster_info import SPClusterInfo
from typing import Optional, Set
from typing_extensions import Self

class ClusterDetails(BaseModel):
    """
    Specifies the array of clusters details including internally and externally claimed clusters
    """ # noqa: E501
    cohesity_clusters: Optional[List[ClusterInfo]] = Field(default=None, description="Specifies the array of clusters upgrade details", alias="cohesityClusters")
    sp_clusters: Optional[List[SPClusterInfo]] = Field(default=None, description="Specifies the array of clusters claimed from IBM Storage Protect environment.", alias="spClusters")
    __properties: ClassVar[List[str]] = ["cohesityClusters", "spClusters"]

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
        """Create an instance of ClusterDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cohesity_clusters (list)
        _items = []
        if self.cohesity_clusters:
            for _item_cohesity_clusters in self.cohesity_clusters:
                if _item_cohesity_clusters:
                    _items.append(_item_cohesity_clusters.to_dict())
            _dict['cohesityClusters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sp_clusters (list)
        _items = []
        if self.sp_clusters:
            for _item_sp_clusters in self.sp_clusters:
                if _item_sp_clusters:
                    _items.append(_item_sp_clusters.to_dict())
            _dict['spClusters'] = _items
        # set to None if cohesity_clusters (nullable) is None
        # and model_fields_set contains the field
        if self.cohesity_clusters is None and "cohesity_clusters" in self.model_fields_set:
            _dict['cohesityClusters'] = None

        # set to None if sp_clusters (nullable) is None
        # and model_fields_set contains the field
        if self.sp_clusters is None and "sp_clusters" in self.model_fields_set:
            _dict['spClusters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cohesityClusters": [ClusterInfo.from_dict(_item) for _item in obj["cohesityClusters"]] if obj.get("cohesityClusters") is not None else None,
            "spClusters": [SPClusterInfo.from_dict(_item) for _item in obj["spClusters"]] if obj.get("spClusters") is not None else None
        })
        return _obj


