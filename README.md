# Face Recognition Attendance System

An intelligent student attendance management system powered by facial recognition technology. This system automates attendance tracking by recognizing students' faces from images or video feeds, providing a secure, accurate, and contactless solution for modern educational institutions.

## 🎯 Features

- **Facial Recognition**: Advanced face detection and identification using state-of-the-art deep learning models
- **Automated Attendance**: Real-time student identification and attendance logging
- **Multi-face Detection**: Handles multiple students in a single image or frame
- **Batch Processing**: Efficiently processes multiple images using multiprocessing
- **Web Interface**: User-friendly dashboard for managing students and viewing attendance records
- **Backend API**: RESTful API for seamless integration with existing systems
- **High Accuracy**: Configurable tolerance levels for optimal recognition accuracy
- **Export Capabilities**: Generate attendance reports in various formats

## 📋 System Architecture

The project is organized into two main components:

```
FaceRecognitionAttendance/
├── student-attendance-system/
│   ├── app/                    # Frontend application
│   ├── backend/                # Backend API and core logic
│   │   ├── face_recognition/   # Face detection & recognition module
│   │   ├── database/           # Database models and queries
│   │   └── api/                # REST API endpoints
│   └── venv/                   # Python virtual environment
└── README.md
```

## 🛠️ Technology Stack

### Backend (90.6% Python)
- **Python**: Core backend language
- **Face Recognition Library**: Deep learning-based facial recognition
- **Flask/FastAPI**: RESTful API framework
- **SQLAlchemy**: Database ORM
- **NumPy/OpenCV**: Image processing and computer vision

### Frontend
- **Web Application**: Interactive dashboard and user interface

### Build & Compilation
- **CMake** (7.3%): Build system configuration
- **C/C++** (1.2%): Performance-critical components
- **Cython** (0.4%): Python-to-C compilation for optimization

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment support
- Face image datasets for training/enrollment

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zaimfazal/FaceRecognitionAttendance.git
   cd FaceRecognitionAttendance
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r student-attendance-system/backend/requirements.txt
   ```

4. **Configure the system**:
   - Set up database configuration
   - Place student face images in designated directories
   - Configure API endpoints and authentication

### Usage

#### Basic Face Recognition

```python
import face_recognition
from PIL import Image

# Load an image
image = face_recognition.load_image_file("student.jpg")

# Get face encodings
face_encodings = face_recognition.face_encodings(image)

# Compare faces
matches = face_recognition.compare_faces(known_encodings, face_encodings[0])
```

#### Running the Backend API

```bash
cd student-attendance-system/backend
python app.py
```

#### Processing Attendance Images

```bash
# Single image processing
python attendance.py known_people_folder/ test_image.jpg

# Batch processing with multiprocessing
python attendance.py known_people_folder/ test_images_dir/ --cpus -1

# Adjust tolerance for accuracy
python attendance.py known_people_folder/ test_image.jpg --tolerance 0.5
```

## 📊 Command Line Options

When running the attendance system:

- `--cpus`: Number of CPU cores for parallel processing (-1 for all available cores)
- `--tolerance`: Face comparison tolerance (0.0-1.0, default: 0.6)
- `--show-distance`: Display face distance metrics for debugging

## 🔧 Configuration

### Tolerance Settings
- **0.6** (default): Balanced accuracy and false positives
- **0.5**: More strict, higher accuracy
- **0.7**: More lenient, fewer false negatives

### Database Setup
Configure your database connection in the backend configuration file.

### API Keys & Authentication
Set up authentication tokens for API access (see backend documentation).

## 📁 Project Structure

```
student-attendance-system/
├── app/                          # Frontend UI
├── backend/
│   ├── main.py                  # Main application entry
│   ├── attendance.py            # Attendance processing logic
│   ├── database.py              # Database models
│   ├── face_recognition.py      # Face recognition engine
│   └── requirements.txt          # Python dependencies
└── venv/                        # Virtual environment
```

## 🎓 How It Works

1. **Enrollment**: Administrator uploads or enrolls student photos
   - System creates facial encodings for each student
   - Encodings are stored securely in the database

2. **Recognition**: During attendance marking
   - Camera/image input is captured
   - Facial detection identifies all faces in the image
   - Each face is encoded and compared with enrolled students

3. **Matching**: System performs face comparison
   - Calculates distance between input and known faces
   - Returns matches within configured tolerance
   - Logs attendance for matched students

4. **Reporting**: Generate attendance records
   - Daily, weekly, monthly reports available
   - Export to CSV, PDF, or database export

## 🔒 Security Considerations

- Face encodings are never reversible to original images
- Secure database encryption recommended for production
- API authentication required for all endpoints
- Audit logs for all attendance changes
- Role-based access control (admin, teacher, student)

## ⚡ Performance Tips

- Use multiprocessing with `--cpus -1` for batch processing
- Optimize tolerance levels based on your use case
- Keep student database indexed for faster lookups
- Regular database maintenance for optimal performance

## 🐛 Troubleshooting

### No faces detected
- Ensure images are clear and well-lit
- Check face size (faces should be at least 100x100 pixels)
- Try lowering tolerance level

### Multiple faces in one image
- System automatically processes all detected faces
- Use `--show-distance` to debug matches

### Slow performance
- Enable multiprocessing with `--cpus -1`
- Consider image preprocessing/resizing
- Use GPU acceleration if available

## 📝 Requirements

See `student-attendance-system/backend/requirements.txt` for complete dependencies:

Key packages:
- face-recognition
- opencv-python
- numpy
- pillow
- sqlalchemy
- click
- (FastAPI/Flask for web framework)

## 📖 API Documentation

Detailed API endpoints and usage:

- `POST /api/attendance/mark` - Mark attendance
- `GET /api/attendance/reports` - Get attendance reports
- `POST /api/students/enroll` - Enroll new student
- `GET /api/students/list` - List all students
- `PUT /api/settings/tolerance` - Adjust tolerance

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is available under the MIT License. See LICENSE file for details.

## 👤 Author

**Zaim Fazal**
- GitHub: [@zaimfazal](https://github.com/zaimfazal)
- Repository: [FaceRecognitionAttendance](https://github.com/zaimfazal/FaceRecognitionAttendance)

## 🙏 Acknowledgments

- Built with the [face_recognition](https://github.com/ageitgey/face_recognition) library
- Powered by dlib's state-of-the-art face detection and recognition
- OpenCV for advanced image processing capabilities

## 📮 Support

For issues, questions, or suggestions:
1. Check existing [Issues](https://github.com/zaimfazal/FaceRecognitionAttendance/issues)
2. Create a new issue with detailed information
3. Include error logs and relevant screenshots

## 🎯 Future Enhancements

- [ ] Real-time video stream processing
- [ ] Mobile app for attendance marking
- [ ] Advanced analytics and insights
- [ ] Integration with student management systems
- [ ] Liveness detection to prevent photo spoofing
- [ ] Multi-factor authentication support
- [ ] Cloud deployment options

---

**Last Updated**: 2025-09-22

For the latest updates, visit the [GitHub Repository](https://github.com/zaimfazal/FaceRecognitionAttendance)
