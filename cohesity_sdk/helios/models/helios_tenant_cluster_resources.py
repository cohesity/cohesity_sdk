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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.helios_source_objects_stats import HeliosSourceObjectsStats
from typing import Set
from typing_extensions import Self

class HeliosTenantClusterResources(BaseModel):
    """
    A list of Sources and Storage Domains assigned to the Tenant, grouped by Cluster.
    """ # noqa: E501
    cluster_identifier: Optional[StrictStr] = Field(default=None, description="Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId.", alias="clusterIdentifier")
    source_names: Optional[List[StrictStr]] = Field(default=None, description="List of completely assigned Sources.", alias="sourceNames")
    source_stats: Optional[List[HeliosSourceObjectsStats]] = Field(default=None, description="Number of assigned objects grouped by source names.", alias="sourceStats")
    storage_domain_names: Optional[List[StrictStr]] = Field(default=None, description="List of assigned Storage Domains.", alias="storageDomainNames")
    __properties: ClassVar[List[str]] = ["clusterIdentifier", "sourceNames", "sourceStats", "storageDomainNames"]

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
        """Create an instance of HeliosTenantClusterResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in source_stats (list)
        _items = []
        if self.source_stats:
            for _item_source_stats in self.source_stats:
                if _item_source_stats:
                    _items.append(_item_source_stats.to_dict())
            _dict['sourceStats'] = _items
        # set to None if cluster_identifier (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_identifier is None and "cluster_identifier" in self.model_fields_set:
            _dict['clusterIdentifier'] = None

        # set to None if source_names (nullable) is None
        # and model_fields_set contains the field
        if self.source_names is None and "source_names" in self.model_fields_set:
            _dict['sourceNames'] = None

        # set to None if source_stats (nullable) is None
        # and model_fields_set contains the field
        if self.source_stats is None and "source_stats" in self.model_fields_set:
            _dict['sourceStats'] = None

        # set to None if storage_domain_names (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_names is None and "storage_domain_names" in self.model_fields_set:
            _dict['storageDomainNames'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosTenantClusterResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterIdentifier": obj.get("clusterIdentifier"),
            "sourceNames": obj.get("sourceNames"),
            "sourceStats": [HeliosSourceObjectsStats.from_dict(_item) for _item in obj["sourceStats"]] if obj.get("sourceStats") is not None else None,
            "storageDomainNames": obj.get("storageDomainNames")
        })
        return _obj


