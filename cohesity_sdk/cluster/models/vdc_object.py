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
from cohesity_sdk.cluster.models.org_vdc_network import OrgVDCNetwork
from cohesity_sdk.cluster.models.vdc_catalog import VdcCatalog
from typing import Set
from typing_extensions import Self

class VdcObject(BaseModel):
    """
    Specifies the details about VMware Virtual datacenter.
    """ # noqa: E501
    catalogs: Optional[List[VdcCatalog]] = Field(default=None, description="Specifies a list of VDC Catalogs.")
    org_networks: Optional[List[OrgVDCNetwork]] = Field(default=None, description="Specifies a list of Organization VDC Networks.", alias="orgNetworks")
    __properties: ClassVar[List[str]] = ["catalogs", "orgNetworks"]

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
        """Create an instance of VdcObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in catalogs (list)
        _items = []
        if self.catalogs:
            for _item_catalogs in self.catalogs:
                if _item_catalogs:
                    _items.append(_item_catalogs.to_dict())
            _dict['catalogs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in org_networks (list)
        _items = []
        if self.org_networks:
            for _item_org_networks in self.org_networks:
                if _item_org_networks:
                    _items.append(_item_org_networks.to_dict())
            _dict['orgNetworks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VdcObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "catalogs": [VdcCatalog.from_dict(_item) for _item in obj["catalogs"]] if obj.get("catalogs") is not None else None,
            "orgNetworks": [OrgVDCNetwork.from_dict(_item) for _item in obj["orgNetworks"]] if obj.get("orgNetworks") is not None else None
        })
        return _obj


