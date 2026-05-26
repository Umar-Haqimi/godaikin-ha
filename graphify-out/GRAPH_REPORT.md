# Graph Report - .  (2026-05-26)

## Corpus Check
- Corpus is ~6,987 words - fits in a single context window. You may not need a graph.

## Summary
- 385 nodes · 511 edges · 66 communities (15 shown, 51 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 51 edges (avg confidence: 0.59)
- Token cost: 60,000 input · 18,813 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Energy Sensor & Coordinator|Energy Sensor & Coordinator]]
- [[_COMMUNITY_Climate Entity|Climate Entity]]
- [[_COMMUNITY_Auth & Config Flow|Auth & Config Flow]]
- [[_COMMUNITY_Cloud API Client|Cloud API Client]]
- [[_COMMUNITY_Translations & Strings|Translations & Strings]]
- [[_COMMUNITY_Mold-Proof Manager|Mold-Proof Manager]]
- [[_COMMUNITY_Shadow State Types|Shadow State Types]]
- [[_COMMUNITY_Integration Bootstrap|Integration Bootstrap]]
- [[_COMMUNITY_Mold-Proof Switch|Mold-Proof Switch]]
- [[_COMMUNITY_Status LED Light|Status LED Light]]
- [[_COMMUNITY_HA Manifest|HA Manifest]]
- [[_COMMUNITY_HACS Manifest|HACS Manifest]]
- [[_COMMUNITY_Icon Config|Icon Config]]
- [[_COMMUNITY_Top-level Config Files|Top-level Config Files]]
- [[_COMMUNITY_Singleton 14|Singleton 14]]
- [[_COMMUNITY_Singleton 15|Singleton 15]]
- [[_COMMUNITY_Singleton 16|Singleton 16]]
- [[_COMMUNITY_Singleton 17|Singleton 17]]
- [[_COMMUNITY_Singleton 18|Singleton 18]]
- [[_COMMUNITY_Singleton 19|Singleton 19]]
- [[_COMMUNITY_Singleton 20|Singleton 20]]
- [[_COMMUNITY_Singleton 21|Singleton 21]]
- [[_COMMUNITY_Singleton 22|Singleton 22]]
- [[_COMMUNITY_Singleton 23|Singleton 23]]
- [[_COMMUNITY_Singleton 24|Singleton 24]]
- [[_COMMUNITY_Singleton 25|Singleton 25]]
- [[_COMMUNITY_Singleton 26|Singleton 26]]
- [[_COMMUNITY_Singleton 27|Singleton 27]]
- [[_COMMUNITY_Singleton 28|Singleton 28]]
- [[_COMMUNITY_Singleton 29|Singleton 29]]
- [[_COMMUNITY_Singleton 30|Singleton 30]]
- [[_COMMUNITY_Singleton 31|Singleton 31]]
- [[_COMMUNITY_Singleton 32|Singleton 32]]
- [[_COMMUNITY_Singleton 33|Singleton 33]]
- [[_COMMUNITY_Singleton 34|Singleton 34]]
- [[_COMMUNITY_Singleton 35|Singleton 35]]
- [[_COMMUNITY_Singleton 36|Singleton 36]]
- [[_COMMUNITY_Singleton 37|Singleton 37]]
- [[_COMMUNITY_Singleton 38|Singleton 38]]
- [[_COMMUNITY_Singleton 40|Singleton 40]]
- [[_COMMUNITY_Singleton 41|Singleton 41]]
- [[_COMMUNITY_Singleton 42|Singleton 42]]
- [[_COMMUNITY_Singleton 43|Singleton 43]]
- [[_COMMUNITY_Singleton 44|Singleton 44]]
- [[_COMMUNITY_Singleton 45|Singleton 45]]
- [[_COMMUNITY_Singleton 46|Singleton 46]]
- [[_COMMUNITY_Singleton 47|Singleton 47]]
- [[_COMMUNITY_Singleton 48|Singleton 48]]
- [[_COMMUNITY_Singleton 49|Singleton 49]]
- [[_COMMUNITY_Singleton 50|Singleton 50]]
- [[_COMMUNITY_Singleton 51|Singleton 51]]
- [[_COMMUNITY_Singleton 52|Singleton 52]]
- [[_COMMUNITY_Singleton 53|Singleton 53]]
- [[_COMMUNITY_Singleton 54|Singleton 54]]
- [[_COMMUNITY_Singleton 55|Singleton 55]]
- [[_COMMUNITY_Singleton 56|Singleton 56]]
- [[_COMMUNITY_Singleton 57|Singleton 57]]
- [[_COMMUNITY_Singleton 58|Singleton 58]]
- [[_COMMUNITY_Singleton 59|Singleton 59]]
- [[_COMMUNITY_Singleton 60|Singleton 60]]
- [[_COMMUNITY_Singleton 61|Singleton 61]]
- [[_COMMUNITY_Singleton 62|Singleton 62]]
- [[_COMMUNITY_Singleton 63|Singleton 63]]
- [[_COMMUNITY_Singleton 64|Singleton 64]]
- [[_COMMUNITY_Singleton 65|Singleton 65]]

## God Nodes (most connected - your core abstractions)
1. `ApiClient` - 26 edges
2. `GodaikinDataUpdateCoordinator` - 24 edges
3. `Aircond` - 20 edges
4. `GodaikinClimate` - 20 edges
5. `AuthClient` - 19 edges
6. `MoldProofManager` - 18 edges
7. `AircondMode` - 11 edges
8. `GodaikinMoldProofSwitch` - 11 edges
9. `GodaikinSensorBase` - 11 edges
10. `validate_input()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `GO DAIKIN README` --references--> `ConfigFlow`  [INFERRED]
  README.md → custom_components/godaikin/config_flow.py
- `GO DAIKIN README` --references--> `AWS Cognito JWT auth pattern`  [EXTRACTED]
  README.md → custom_components/godaikin/auth.py
- `GO DAIKIN README` --references--> `Simulated mold-proof behavior`  [EXTRACTED]
  README.md → custom_components/godaikin/mold_proof.py
- `GO DAIKIN README` --references--> `AuthClient`  [EXTRACTED]
  README.md → custom_components/godaikin/auth.py
- `GO DAIKIN README` --references--> `MoldProofManager`  [EXTRACTED]
  README.md → custom_components/godaikin/mold_proof.py

## Hyperedges (group relationships)
- **Mold-proof lifecycle (climate UI, manager, API control)** — godaikin_climate_async_set_hvac_mode, godaikin_mold_proof_manager, godaikin_api_apiclient_set_mode, godaikin_api_apiclient_set_fan_mode, godaikin_switch_godaikinmoldproofswitch [INFERRED 0.85]
- **HA polling pipeline: Coordinator polls API, accumulates energy, feeds entities** — godaikin_coordinator_async_update_data, godaikin_api_apiclient_get_airconds, godaikin_energy_energycounter_accumulate, godaikin_sensor_godaikinsensorbase, godaikin_climate_godaikinclimate [INFERRED 0.85]
- **Cognito auth token flow used by all API calls** — godaikin_auth_authclient_async_get_jwt_token, godaikin_auth_cognitotoken, godaikin_api_apiclient_api_request [EXTRACTED 1.00]

## Communities (66 total, 51 thin omitted)

### Community 0 - "Energy Sensor & Coordinator"
Cohesion: 0.06
Nodes (35): GodaikinDataUpdateCoordinator.get_energy_usage, GodaikinDataUpdateCoordinator, Class to manage fetching GO DAIKIN data., Initialize the coordinator., Fetch data from GO DAIKIN API., Get energy usage for an air conditioner., async_get_config_entry_diagnostics(), Return diagnostics for a config entry. (+27 more)

### Community 1 - "Climate Entity"
Cohesion: 0.06
Nodes (24): ClimateEntity, async_setup_entry(), fan_mode(), GodaikinClimate, hvac_mode(), Climate platform for GO DAIKIN integration., Set new target temperature., Set new horizontal swing mode. (+16 more)

### Community 2 - "Auth & Config Flow"
Cohesion: 0.09
Nodes (32): AWS Cognito JWT auth pattern, Simulated mold-proof behavior, Exception, async_reload_entry (init), async_setup_entry (init), async_unload_entry (init), AuthClient, AuthError (+24 more)

### Community 3 - "Cloud API Client"
Cohesion: 0.1
Nodes (17): ApiClient, GodaikinClimate.async_set_fan_mode, GodaikinClimate.async_set_hvac_mode, GodaikinClimate.async_set_preset_mode, GodaikinClimate.async_set_swing_horizontal_mode, GodaikinClimate.async_set_swing_mode, GodaikinClimate.async_set_temperature, GodaikinClimate.async_turn_off (+9 more)

### Community 4 - "Translations & Strings"
Cohesion: 0.07
Nodes (28): already_configured, config, abort, error, step, mold_proof_duration, mold_proof_duration, password (+20 more)

### Community 5 - "Mold-Proof Manager"
Cohesion: 0.09
Nodes (14): MoldProofManager, Start mold-proof operation for a device., Cancel active mold-proof operation., Interrupt mold-proof and return if it was active and previous fan speed., Get the mold-proof state for a device., Get remaining mold-proof time in seconds., Manage mold-proof operations for air conditioners., Initialize the mold-proof manager. (+6 more)

### Community 6 - "Shadow State Types"
Cohesion: 0.1
Nodes (10): AWS IoT shadow state protocol, Enum, GodaikinDataUpdateCoordinator._async_update_data, EnergyCounter.accumulate_energy_usage_for_aircond, AircondPreset, AircondState, from_api(), from_dict() (+2 more)

### Community 7 - "Integration Bootstrap"
Cohesion: 0.14
Nodes (13): print_aircond(), API Client for interacting with the GO DAIKIN cloud service., # NOTE: unused for now - getacgraphdata API isn't timely with new data. Kept for, Constants for the GO DAIKIN integration., GO DAIKIN Data Update Coordinator., Diagnostics support for GO DAIKIN., async_reload_entry(), async_setup_entry() (+5 more)

### Community 8 - "Mold-Proof Switch"
Cohesion: 0.11
Nodes (11): MoldProofManager.cancel_mold_proof, MoldProofManager.set_enabled, async_setup_entry(), GodaikinMoldProofSwitch, Switch platform for GO DAIKIN integration., Disable mold-proof for this device., Set up GO DAIKIN switch entities from a config entry., Representation of GO DAIKIN mold-proof switch. (+3 more)

### Community 9 - "Status LED Light"
Cohesion: 0.12
Nodes (9): async_setup_entry(), GodaikinStatusLED, Light platform for GO DAIKIN integration., Set up GO DAIKIN light entities from a config entry., Representation of GO DAIKIN status LED., Initialize the status LED., Turn the status LED on., Turn the status LED off. (+1 more)

### Community 10 - "HA Manifest"
Cohesion: 0.17
Nodes (11): codeowners, config_flow, dependencies, documentation, domain, integration_type, iot_class, issue_tracker (+3 more)

### Community 11 - "HACS Manifest"
Cohesion: 0.4
Nodes (4): content_in_root, homeassistant, name, render_readme

### Community 12 - "Icon Config"
Cohesion: 0.5
Nodes (3): domain, icon, name

### Community 13 - "Top-level Config Files"
Cohesion: 0.5
Nodes (4): DOMAIN constant, HACS manifest, godaikin icon.json, godaikin manifest.json

## Knowledge Gaps
- **175 isolated node(s):** `Standalone test harness for the GO DAIKIN API client.  Loads auth.py, api.py, an`, `name`, `content_in_root`, `render_readme`, `homeassistant` (+170 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **51 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `GodaikinDataUpdateCoordinator` connect `Energy Sensor & Coordinator` to `Climate Entity`, `Auth & Config Flow`, `Cloud API Client`, `Mold-Proof Manager`, `Integration Bootstrap`, `Mold-Proof Switch`, `Status LED Light`?**
  _High betweenness centrality (0.193) - this node is a cross-community bridge._
- **Why does `ApiClient` connect `Cloud API Client` to `Energy Sensor & Coordinator`, `Auth & Config Flow`, `Integration Bootstrap`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `MoldProofManager` connect `Mold-Proof Manager` to `Energy Sensor & Coordinator`, `Climate Entity`, `Integration Bootstrap`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `ApiClient` (e.g. with `ConfigFlow` and `CannotConnect`) actually correct?**
  _`ApiClient` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `GodaikinDataUpdateCoordinator` (e.g. with `AuthClient` and `Aircond`) actually correct?**
  _`GodaikinDataUpdateCoordinator` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Aircond` (e.g. with `GodaikinDataUpdateCoordinator` and `GodaikinSensorBase`) actually correct?**
  _`Aircond` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `GodaikinClimate` (e.g. with `AircondMode` and `AircondPreset`) actually correct?**
  _`GodaikinClimate` has 4 INFERRED edges - model-reasoned connections that need verification._