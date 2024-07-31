import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { ConfirmationDialogService } from '../confirmation-dialog/confirmation-dialog.service';
import { AgentService } from '../service/agent.service';
import { GlobalConstants } from 'src/environments/GlobalConstants';
import { GlobalMethods } from 'src/environments/GlobalMethods';
import { DialogSimpleComponent } from '../dialog/dialog-simple';

@Component({
  selector: 'app-donate-form',
  templateUrl: './donate-form.component.html',
  styleUrls: ['./donate-form.component.scss']
})
export class DonateFormComponent implements OnInit {
  dialog: any;
  form: any;
  isButtonDisabled: any;
  spinner: any;

  hyperlink: any;
  url: any;
  noURL: any;

  constructor(
    private dialogComponent: DialogSimpleComponent,
    private route: ActivatedRoute,
    private formBuilder: FormBuilder,
    private confirmationDialogService: ConfirmationDialogService,
    private agentService: AgentService,
  ) { }

  ngOnInit(): void {
    this.initForm();
  }

  verify() {
    this.spinner = true;
    }

  initForm() {
    this.form = this.formBuilder.group({
      email: [undefined],
      desc: [undefined],
    });
    
  }

  copyInputMessage(inputElement: any){
    inputElement.select();
    document.execCommand('copy');
    inputElement.setSelectionRange(0, 0);
  }

  onSubmit() {
    this.spinner = true;
    let email = this.form.value.email;

    console.log('email--> ', email);
    console.log('form data--> ', this.form.value);

    let serializedForm = JSON.stringify(this.form.value);
    console.log('serializedForm: ', this.form.value);
  
    this.form.patchValue(serializedForm);
  
    this.agentService.donatePost(serializedForm).subscribe((data: any) => {
      console.log("data===>" + data);
      this.spinner = undefined;

      this.dialogComponent.openDialog("Form submitted successfully. We will get back to you.");  
    }
      ,
      (error: { error: { message: string; }; }) => {
        console.log(error);  
       this.dialogComponent.openDialog(GlobalMethods.getError(error));    
      }
    );

  }
}

