# Timelapse Automation Notes

## Goals
- Sunset-relative frame selection
- Camera drift detection
- Video stabilization

## Modules
- OpenCV for frame analysis
- Home Assistant for entity tracking
- Python scripts for scheduling and ingestion

## Workflow
1. Detect sunset time via Home Assistant
2. Schedule frame capture ± offset
3. Analyze drift and stabilize frames
4. Archive with hash-based deduplication

## Status
- `timelapse-test.py` staged
- Awaiting Copilot Chat activation for inline doc generation
