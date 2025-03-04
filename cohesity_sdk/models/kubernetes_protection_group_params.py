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
from cohesity_sdk.models.kubernetes_filter_params import KubernetesFilterParams
from cohesity_sdk.models.kubernetes_protection_group_object_params import KubernetesProtectionGroupObjectParams
from cohesity_sdk.models.vlan_params import VlanParams
from typing import Optional, Set
from typing_extensions import Self

class KubernetesProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are related to Kubernetes Protection Groups.
    """ # noqa: E501
    exclude_label_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of arrays of label IDs that specify labels to exclude. Optionally specify a list of labels to exclude from protecting by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the Cluster generates a list of namespaces to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array.", alias="excludeLabelIds")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    exclude_params: Optional[KubernetesFilterParams] = Field(default=None, alias="excludeParams")
    include_params: Optional[KubernetesFilterParams] = Field(default=None, alias="includeParams")
    label_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of array of label IDs that specify labels to protect. Optionally specify a list of labels to protect by listing protection source ids of labels in this two dimensional array. Using this two dimensional array of label IDs, the cluster generates a list of namespaces to protect, which are derived from intersections of the inner arrays and union of the outer array.", alias="labelIds")
    leverage_csi_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies if CSI snapshots should be used for backup of namespaces.", alias="leverageCSISnapshot")
    objects: Optional[List[KubernetesProtectionGroupObjectParams]] = Field(default=None, description="Specifies the objects included in the Protection Group.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    vlan_params: Optional[VlanParams] = Field(default=None, alias="vlanParams")
    __properties: ClassVar[List[str]] = ["excludeLabelIds", "excludeObjectIds", "excludeParams", "includeParams", "labelIds", "leverageCSISnapshot", "objects", "sourceId", "sourceName", "vlanParams"]

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
        """Create an instance of KubernetesProtectionGroupParams from a JSON string"""
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
            "source_id",
            "source_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of exclude_params
        if self.exclude_params:
            _dict['excludeParams'] = self.exclude_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of include_params
        if self.include_params:
            _dict['includeParams'] = self.include_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of vlan_params
        if self.vlan_params:
            _dict['vlanParams'] = self.vlan_params.to_dict()
        # set to None if exclude_params (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_params is None and "exclude_params" in self.model_fields_set:
            _dict['excludeParams'] = None

        # set to None if include_params (nullable) is None
        # and model_fields_set contains the field
        if self.include_params is None and "include_params" in self.model_fields_set:
            _dict['includeParams'] = None

        # set to None if label_ids (nullable) is None
        # and model_fields_set contains the field
        if self.label_ids is None and "label_ids" in self.model_fields_set:
            _dict['labelIds'] = None

        # set to None if leverage_csi_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.leverage_csi_snapshot is None and "leverage_csi_snapshot" in self.model_fields_set:
            _dict['leverageCSISnapshot'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KubernetesProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeLabelIds": obj.get("excludeLabelIds"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "excludeParams": KubernetesFilterParams.from_dict(obj["excludeParams"]) if obj.get("excludeParams") is not None else None,
            "includeParams": KubernetesFilterParams.from_dict(obj["includeParams"]) if obj.get("includeParams") is not None else None,
            "labelIds": obj.get("labelIds"),
            "leverageCSISnapshot": obj.get("leverageCSISnapshot"),
            "objects": [KubernetesProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "vlanParams": VlanParams.from_dict(obj["vlanParams"]) if obj.get("vlanParams") is not None else None
        })
        return _obj


