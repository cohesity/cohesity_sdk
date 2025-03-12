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
from cohesity_sdk.helios.models.helios_archival_config import HeliosArchivalConfig
from cohesity_sdk.helios.models.helios_cloud_spin_config import HeliosCloudSpinConfig
from cohesity_sdk.helios.models.helios_common_target_configuration import HeliosCommonTargetConfiguration
from cohesity_sdk.helios.models.helios_replication_config import HeliosReplicationConfig
from cohesity_sdk.helios.models.helios_rpaas_config import HeliosRpaasConfig
from typing import Set
from typing_extensions import Self

class HeliosTargetsConfiguration(BaseModel):
    """
    Specifies the replication, archival and cloud spin targets of Protection Policy.
    """ # noqa: E501
    archival_targets: Optional[List[HeliosArchivalConfig]] = Field(default=None, alias="archivalTargets")
    cloud_spin_targets: Optional[List[HeliosCloudSpinConfig]] = Field(default=None, alias="cloudSpinTargets")
    onprem_deploy_targets: Optional[List[HeliosCommonTargetConfiguration]] = Field(default=None, alias="onpremDeployTargets")
    replication_targets: Optional[List[HeliosReplicationConfig]] = Field(default=None, alias="replicationTargets")
    rpaas_targets: Optional[List[HeliosRpaasConfig]] = Field(default=None, alias="rpaasTargets")
    __properties: ClassVar[List[str]] = ["archivalTargets", "cloudSpinTargets", "onpremDeployTargets", "replicationTargets", "rpaasTargets"]

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
        """Create an instance of HeliosTargetsConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in archival_targets (list)
        _items = []
        if self.archival_targets:
            for _item_archival_targets in self.archival_targets:
                if _item_archival_targets:
                    _items.append(_item_archival_targets.to_dict())
            _dict['archivalTargets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cloud_spin_targets (list)
        _items = []
        if self.cloud_spin_targets:
            for _item_cloud_spin_targets in self.cloud_spin_targets:
                if _item_cloud_spin_targets:
                    _items.append(_item_cloud_spin_targets.to_dict())
            _dict['cloudSpinTargets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in onprem_deploy_targets (list)
        _items = []
        if self.onprem_deploy_targets:
            for _item_onprem_deploy_targets in self.onprem_deploy_targets:
                if _item_onprem_deploy_targets:
                    _items.append(_item_onprem_deploy_targets.to_dict())
            _dict['onpremDeployTargets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in replication_targets (list)
        _items = []
        if self.replication_targets:
            for _item_replication_targets in self.replication_targets:
                if _item_replication_targets:
                    _items.append(_item_replication_targets.to_dict())
            _dict['replicationTargets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rpaas_targets (list)
        _items = []
        if self.rpaas_targets:
            for _item_rpaas_targets in self.rpaas_targets:
                if _item_rpaas_targets:
                    _items.append(_item_rpaas_targets.to_dict())
            _dict['rpaasTargets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosTargetsConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTargets": [HeliosArchivalConfig.from_dict(_item) for _item in obj["archivalTargets"]] if obj.get("archivalTargets") is not None else None,
            "cloudSpinTargets": [HeliosCloudSpinConfig.from_dict(_item) for _item in obj["cloudSpinTargets"]] if obj.get("cloudSpinTargets") is not None else None,
            "onpremDeployTargets": [HeliosCommonTargetConfiguration.from_dict(_item) for _item in obj["onpremDeployTargets"]] if obj.get("onpremDeployTargets") is not None else None,
            "replicationTargets": [HeliosReplicationConfig.from_dict(_item) for _item in obj["replicationTargets"]] if obj.get("replicationTargets") is not None else None,
            "rpaasTargets": [HeliosRpaasConfig.from_dict(_item) for _item in obj["rpaasTargets"]] if obj.get("rpaasTargets") is not None else None
        })
        return _obj


