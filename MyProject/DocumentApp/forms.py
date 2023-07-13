from django import forms
from .models import Documents


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = "__all__"

        lables = {
            "pan_card": "Pan Card",
            "aadhar_card": "Aaadhar Card",
            "bank_statment": "Bank Statment",
            "photo": "Photo",
            "signature": "Signature",
            "salary_slip": "Salary Slip",
            "from16": "From16",
            "blance_sheet": "Blance Sheet",
            "itr": "Itr",
            "business_proof": "Business Proof",
        }

        widgets = {"customer": forms.TextInput(attrs={"readonly": "readonly"})}
