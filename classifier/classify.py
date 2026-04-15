def classify_job(title):
    t = title.lower()
    if any(w in t for w in ['walk-in', 'walk in', 'walkin']):
        return 'Walk-in Interview'
    elif any(w in t for w in ['tender', 'quotation', 'bid']):
        return 'Tender'
    elif any(w in t for w in ['jrf', 'srf', 'project associate',
                               'research associate', 'intern']):
        return 'Internship/JRF'
    elif any(w in t for w in ['professor', 'faculty', 'lecturer',
                               'assistant prof', 'associate prof']):
        return 'Faculty'
    elif any(w in t for w in ['dean', 'registrar', 'director', 'vc']):
        return 'Admin Post'
    else:
        return 'Other'
