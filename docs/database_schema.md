# Database Schema Documentation

This document outlines the database schema for the project management module. The models are designed based on the principles of Domain-Driven Design (DDD), where each model represents a clear entity within the project domain.

## Models

The core models of this module are:

-   **Project**: Represents a high-level project.
-   **Phase**: Represents a phase within a project.
-   **Activity**: Represents a task or activity within a phase.
-   **Dependency**: Represents a dependency between two activities.

---

### 1. `Project` Model

Represents a single project.

**Fields:**

| Field         | Type                      | Description                                | Notes                                                 |
|---------------|---------------------------|--------------------------------------------|-------------------------------------------------------|
| `name`        | `CharField(255)`          | The name of the project.                   | Required.                                             |
| `code`        | `CharField(50)`           | A unique code for the project.             | Required, Unique.                                     |
| `description` | `TextField`               | A detailed description of the project.     | Optional.                                             |
| `employer`    | `ForeignKey(User)`        | The user who is the employer for the project.| `on_delete=models.PROTECT`                            |
| `start_date`  | `DateField`               | The planned start date of the project.     | Required.                                             |
| `end_date`    | `DateField`               | The planned end date of the project.       | Required.                                             |
| `progress`    | `PositiveIntegerField`    | The completion progress in percentage.     | Default: 0.                                           |
| `status`      | `CharField(20)`           | The current status of the project.         | Choices: `planning`, `in_progress`, etc. Default: `planning`. |
| `lat`         | `FloatField`              | The latitude for the project's location.   | Optional.                                             |
| `lng`         | `FloatField`              | The longitude for the project's location.  | Optional.                                             |
| `created_at`  | `DateTimeField`           | The timestamp when the project was created. | Auto-generated.                                       |
| `updated_at`  | `DateTimeField`           | The timestamp of the last update.          | Auto-updated.                                         |

---

### 2. `Phase` Model

Represents a distinct phase within a `Project`.

**Fields:**

| Field         | Type                      | Description                                | Notes                                                 |
|---------------|---------------------------|--------------------------------------------|-------------------------------------------------------|
| `name`        | `CharField(255)`          | The name of the phase.                     | Required.                                             |
| `code`        | `CharField(50)`           | A unique code for the phase.               | Required, Unique.                                     |
| `description` | `TextField`               | A detailed description of the phase.       | Optional.                                             |
| `project`     | `ForeignKey(Project)`     | The project this phase belongs to.         | `on_delete=models.CASCADE`                            |
| `start_date`  | `DateField`               | The planned start date of the phase.       | Required.                                             |
| `end_date`    | `DateField`               | The planned end date of the phase.         | Required.                                             |
| `progress`    | `PositiveIntegerField`    | The completion progress in percentage.     | Default: 0.                                           |
| `status`      | `CharField(20)`           | The current status of the phase.           | Choices: `planning`, `in_progress`, etc. Default: `planning`. |
| `created_at`  | `DateTimeField`           | The timestamp when the phase was created.   | Auto-generated.                                       |
| `updated_at`  | `DateTimeField`           | The timestamp of the last update.          | Auto-updated.                                         |

**Constraints:**
- A phase's `name` must be unique within its `project`.

---

### 3. `Activity` Model

Represents a specific task or activity within a `Phase`.

**Fields:**

| Field             | Type                      | Description                                    | Notes                                                 |
|-------------------|---------------------------|------------------------------------------------|-------------------------------------------------------|
| `name`            | `CharField(255)`          | The name of the activity.                      | Required.                                             |
| `code`            | `CharField(50)`           | A unique code for the activity.                | Required, Unique.                                     |
| `description`     | `TextField`               | A detailed description of the activity.        | Optional.                                             |
| `phase`           | `ForeignKey(Phase)`       | The phase this activity belongs to.            | `on_delete=models.CASCADE`                            |
| `parent_activity` | `ForeignKey('self')`      | The parent activity (for sub-activities).      | Optional, allows for hierarchical activities.         |
| `start_date`      | `DateField`               | The planned start date of the activity.        | Required.                                             |
| `end_date`        | `DateField`               | The planned end date of the activity.          | Required.                                             |
| `progress`        | `PositiveIntegerField`    | The completion progress in percentage.         | Default: 0.                                           |
| `status`          | `CharField(20)`           | The current status of the activity.            | Choices: `planning`, `in_progress`, etc. Default: `planning`. |
| `created_at`      | `DateTimeField`           | The timestamp when the activity was created.   | Auto-generated.                                       |
| `updated_at`      | `DateTimeField`           | The timestamp of the last update.              | Auto-updated.                                         |

**Constraints:**
- An activity's `name` must be unique within its `phase`.

---

### 4. `Dependency` Model

Defines a dependency relationship between two `Activity` instances.

**Fields:**

| Field             | Type                  | Description                                      | Notes                                      |
|-------------------|-----------------------|--------------------------------------------------|--------------------------------------------|
| `activity`        | `ForeignKey(Activity)`| The main activity.                               | The activity that has a dependency.        |
| `depends_on`      | `ForeignKey(Activity)`| The activity that must be completed first.       | The prerequisite activity.                 |
| `dependency_type` | `CharField(20)`       | The type of dependency (e.g., Finish-to-Start).  | Choices: `finish_to_start`, `start_to_start`, etc. |

**Constraints:**
- The combination of `activity`, `depends_on`, and `dependency_type` must be unique.
